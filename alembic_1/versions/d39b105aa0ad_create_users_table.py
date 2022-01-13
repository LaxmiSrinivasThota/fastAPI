"""create users table

Revision ID: d39b105aa0ad
Revises: b4d0812597d6
Create Date: 2022-01-13 02:06:36.464802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd39b105aa0ad'
down_revision = 'b4d0812597d6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',sa.Column('id', sa.Integer(), nullable=False),
                            sa.Column('email', sa.String(), nullable=False), 
                            sa.Column('password', sa.String(), nullable=False), 
                            sa.Column('created_at', sa.TIMESTAMP(timezone=True) ,server_default=sa.text('now()'), nullable=False), 
                            sa.PrimaryKeyConstraint('id'), 
                            sa.UniqueConstraint('email')
                            )
    pass

def downgrade():
    op.drop_table('users')
    pass
