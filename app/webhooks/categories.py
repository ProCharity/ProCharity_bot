from flask import request, jsonify, make_response, Response
from http import HTTPStatus
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import load_only
from flask_restful import Resource
from flask_apispec.views import MethodResource
from flask_apispec import doc
from pydantic import parse_obj_as, ValidationError
from werkzeug.exceptions import HTTPException


from app.database import db_session
from app.logger import webhooks_logger as logger
from app.models import Category
from app.request_models.category import CategoryCreateRequest
from app.webhooks.check_webhooks_token import check_webhooks_token


class CreateCategories(MethodResource, Resource):
    method_decorators = {'post': [check_webhooks_token]}
    @doc(description='Сreates Categories in the database',
         tags=['Create categories'],
         params={'token': {
             'description': 'webhooks token',
             'in': 'header',
             'type': 'string',
             'required': True
         }})
    def post(self):
        categories = request_to_context(CategoryCreateRequest, request)

        categories_dict = {int(category.id): category for category in categories}
        categories_db = Category.query.options(load_only('archive')).all()

        category_id_json = [int(member.id) for member in categories]
        category_id_db = [member.id for member in categories_db]

        category_id_db_not_archive = [member.id for member in categories_db if member.archive == False]
        category_id_db_archive = list(set(category_id_db) - set(category_id_db_not_archive))

        category_for_unarchive = list(set(category_id_db_archive) & set(category_id_json))
        category_for_adding_db = list(set(category_id_json) - set(category_id_db))
        category_for_archive = list(set(category_id_db_not_archive) - set(category_id_json))

        for category in categories:
            if int(category.id) in category_for_adding_db:
                c = Category(
                    id=category.id,
                    name=category.name,
                    archive=False,
                    parent_id=category.parent_id
                )
                db_session.add(c)

        archive_records = [category for category in categories_db if category.id in category_for_archive]
        for category in archive_records:
            category.archive = True
        unarchive_records = [category for category in categories_db if category.id in category_for_unarchive]

        categories_for_update = list(
            set(category_id_json) - set(category_for_archive) - set(category_for_adding_db))

        active_category = [category for category in categories_db if category.id in categories_for_update]

        if active_category:
            self.__update_active_category(active_category, categories_dict)

        for task in unarchive_records:
            task.archive = False

        try:
            db_session.commit()
        except SQLAlchemyError as ex:
            logger.error(f'Categories: Database commit error "{str(ex)}"')
            db_session.rollback()
            return make_response(jsonify(message=f"Bad request: {str(ex)}"), 400)

        logger.info("Categories: New categories successfully added.")
        return make_response(jsonify(result='ok'), 200)

    def __hash__(self, category):
        if type(category) == dict:
            id = category.get('id')
            name = category.get('name')
            parent_id = category.get('parent_id')
            return hash(f'{id}{name}{parent_id}')
        return hash(f'{category.id}{category.name}{category.parent_id}')

    def __update_active_category(self, active_category, categories):
        for category in active_category:
            category_from_dict = categories.get(category.id)
            if self.__hash__(category) != self.__hash__(category_from_dict):
                self.__update_category_fields(category, category_from_dict)

    def __update_category_fields(self, category, category_from_dict):
        category.name = category_from_dict['name']
        category.parent_id = category_from_dict['parent_id']
        category.archive = False


def request_to_context(context, request):
    if not request.json:
        logger.error(f'{context}: Json contains no data')
        raise HTTPException(f'Json contains no data, {HTTPStatus.BAD_REQUEST}')
    try:
        request_data = parse_obj_as(list[context], obj=request.json)
        return request_data
    except ValidationError as error:
        logger.error(error)
        raise HTTPException(f'ValidationError: {error}, {HTTPStatus.BAD_REQUEST}') from error
 