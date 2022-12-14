"""removed link column

Revision ID: 4923464af32d
Revises: 5bc1bf4520d8
Create Date: 2022-12-04 17:08:27.106714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4923464af32d'
down_revision = '5bc1bf4520d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_orders')
    op.drop_table('orders')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('bookId', sa.INTEGER(), nullable=False),
    sa.Column('orderDate', sa.DATETIME(), nullable=True),
    sa.Column('userId', sa.VARCHAR(length=20), nullable=False),
    sa.Column('review', sa.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bookId')
    )
    op.create_table('_alembic_tmp_orders',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('bookId', sa.INTEGER(), nullable=False),
    sa.Column('orderDate', sa.DATETIME(), nullable=True),
    sa.Column('review', sa.VARCHAR(length=200), nullable=True),
    sa.Column('userIdId', sa.VARCHAR(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bookId')
    )
    # ### end Alembic commands ###
