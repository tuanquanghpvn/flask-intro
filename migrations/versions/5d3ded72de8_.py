"""empty message

Revision ID: 5d3ded72de8
Revises: f59bfd5312e
Create Date: 2015-11-30 13:51:40.741708

"""

# revision identifiers, used by Alembic.
revision = '5d3ded72de8'
down_revision = 'f59bfd5312e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('staff', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'staff')
    op.drop_column('user', 'active')
    ### end Alembic commands ###
