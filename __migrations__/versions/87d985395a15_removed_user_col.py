"""removed user col

Revision ID: 87d985395a15
Revises: 1302ff64da54
Create Date: 2022-12-05 00:57:10.411097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87d985395a15'
down_revision = '1302ff64da54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_column('user')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user', sa.VARCHAR(length=200), nullable=True))

    # ### end Alembic commands ###