import os

from flask import send_file, request, jsonify, make_response
from flask_apispec import doc
from flask_apispec.views import MethodResource
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app import config
from app.logger import app_logger as logger


class DownloadLogs(MethodResource, Resource):
    @doc(description='Download logs',
         tags=['Download log files'],
         params={
             'log_file': {
                 'description': 'app_logs, bot_logs or webhook_logs',
                 'in': 'query',
                 'type': 'string',
                 'required': True},
             'Authorization': config.PARAM_HEADER_AUTH})     
    @jwt_required()
    def get(self):
        log_file = request.args.get('log_file')
        directory = f"../logs/{log_file}"
        try:
            return send_file(directory, as_attachment=True)
        except FileNotFoundError:
            logger.info(f'Download log files: incorrect file_name "{log_file}"')
            return 'Make sure you pass in the correct log_file'


class GetListLogFiles(MethodResource, Resource):        # TODO: название, описание
    @doc(description='.............', 
         tags=['.............'],
         params={
             'Authorization': config.PARAM_HEADER_AUTH})     
    @jwt_required()
    def get(self):
        all_log_files = os.listdir(path='./logs')
        return make_response(jsonify(all_log_files=all_log_files), 200)
