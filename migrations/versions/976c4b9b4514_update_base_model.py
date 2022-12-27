"""Update Base model

Revision ID: 976c4b9b4514
Revises: 87c7d29e3ddb
Create Date: 2022-12-26 12:56:27.764392

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '976c4b9b4514'
down_revision = '87c7d29e3ddb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('admin_token_requests', sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('admin_token_requests', sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('admin_token_requests', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('admin_users', sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('admin_users', sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('admin_users', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('categories', sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('categories', sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('categories', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('external_site_users', sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('external_site_users', sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('external_site_users', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('notifications', sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('notifications', sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('notifications', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('reasons_canceling', sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('reasons_canceling', sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('reasons_canceling', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('statistics', sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('statistics', sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('statistics', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('tasks', sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('tasks', sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('tasks', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.execute('UPDATE tasks SET created_at = created_date')
    op.execute('UPDATE tasks SET updated_at = updated_date')
    op.add_column('users', sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('users', sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('users', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    op.add_column('users_categories', sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('users_categories', sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True))
    op.add_column('users_categories', sa.Column('is_deleted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users_categories', sa.Column('audit_id_users_categories', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_categories_audit_id_users_categories_fkey', 'users_categories', 'base_audit', ['audit_id_users_categories'], ['id'])
    op.drop_column('users_categories', 'is_deleted')
    op.drop_column('users_categories', 'updated_at')
    op.drop_column('users_categories', 'created_at')
    op.drop_column('users', 'is_deleted')
    op.drop_column('users', 'updated_at')
    op.drop_column('users', 'created_at')
    op.drop_column('tasks', 'is_deleted')
    op.drop_column('tasks', 'updated_at')
    op.drop_column('tasks', 'created_at')
    op.drop_column('statistics', 'is_deleted')
    op.drop_column('statistics', 'updated_at')
    op.drop_column('statistics', 'created_at')
    op.drop_column('reasons_canceling', 'is_deleted')
    op.drop_column('reasons_canceling', 'updated_at')
    op.drop_column('reasons_canceling', 'created_at')
    op.drop_column('notifications', 'is_deleted')
    op.drop_column('notifications', 'updated_at')
    op.drop_column('notifications', 'created_at')
    op.drop_column('external_site_users', 'is_deleted')
    op.drop_column('external_site_users', 'updated_at')
    op.drop_column('external_site_users', 'created_at')
    op.drop_column('categories', 'is_deleted')
    op.drop_column('categories', 'updated_at')
    op.drop_column('categories', 'created_at')
    op.drop_column('admin_users', 'is_deleted')
    op.drop_column('admin_users', 'updated_at')
    op.drop_column('admin_users', 'created_at')
    op.drop_column('admin_token_requests', 'is_deleted')
    op.drop_column('admin_token_requests', 'updated_at')
    op.drop_column('admin_token_requests', 'created_at')
    # ### end Alembic commands ###
