"""empty message

Revision ID: 42925b8fbb86
Revises: 192e5c4782f0
Create Date: 2015-11-26 10:23:38.456123

"""

# revision identifiers, used by Alembic.
revision = '42925b8fbb86'
down_revision = '192e5c4782f0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('content', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'content')
    ### end Alembic commands ###
