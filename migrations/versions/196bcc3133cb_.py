"""empty message

Revision ID: 196bcc3133cb
Revises: 5d3ded72de8
Create Date: 2015-11-30 13:53:29.212438

"""

# revision identifiers, used by Alembic.
revision = '196bcc3133cb'
down_revision = '5d3ded72de8'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.alter_column('user', 'staff',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'staff',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('user', 'active',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    ### end Alembic commands ###
