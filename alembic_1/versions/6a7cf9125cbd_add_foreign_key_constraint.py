"""add foreign key constraint

Revision ID: 6a7cf9125cbd
Revises: d39b105aa0ad
Create Date: 2022-01-13 02:08:16.549109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a7cf9125cbd'
down_revision = 'd39b105aa0ad'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['user_id'], remote_cols=['id'], ondelete="CASCADE")
    pass

def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts','user_id')
    pass
