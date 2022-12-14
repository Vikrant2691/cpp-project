"""removed link column

Revision ID: f252359fbb04
Revises: 38e707558de5
Create Date: 2022-12-04 16:47:09.920338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f252359fbb04'
down_revision = '38e707558de5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products_info', schema=None) as batch_op:
        batch_op.drop_column('link')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products_info', schema=None) as batch_op:
        batch_op.add_column(sa.Column('link', sa.VARCHAR(length=200), nullable=False))

    # ### end Alembic commands ###
