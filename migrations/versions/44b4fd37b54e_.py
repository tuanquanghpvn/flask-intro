"""empty message

Revision ID: 44b4fd37b54e
Revises: 293c6eae1bb7
Create Date: 2015-12-01 09:12:21.569936

"""

# revision identifiers, used by Alembic.
revision = '44b4fd37b54e'
down_revision = '293c6eae1bb7'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('is_staff', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    op.drop_column('user', 'active')
    op.drop_column('user', 'superuser')
    op.drop_column('user', 'staff')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('staff', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('superuser', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_column('user', 'is_superuser')
    op.drop_column('user', 'is_staff')
    op.drop_column('user', 'is_active')
    ### end Alembic commands ###