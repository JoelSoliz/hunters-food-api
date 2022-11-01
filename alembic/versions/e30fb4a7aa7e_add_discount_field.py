"""Add discount field

Revision ID: e30fb4a7aa7e
Revises: 26499508eb43
Create Date: 2022-10-17 18:58:10.174469

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e30fb4a7aa7e'
down_revision = '26499508eb43'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('name', sa.String(length=100), nullable=False))
    op.add_column('product', sa.Column('product_type', sa.String(length=100), nullable=False))
    op.add_column('product', sa.Column('image', sa.BLOB(), nullable=False))
    op.add_column('product', sa.Column('discount', sa.FLOAT(precision=10.2), nullable=True))
    op.drop_constraint('product_ibfk_2', 'product', type_='foreignkey')
    op.drop_column('product', 'image_product')
    op.drop_column('product', 'name_product')
    op.drop_column('product', 'id_product_type')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('id_product_type', mysql.VARCHAR(length=4), nullable=True))
    op.add_column('product', sa.Column('name_product', mysql.VARCHAR(length=100), nullable=False))
    op.add_column('product', sa.Column('image_product', sa.BLOB(), nullable=False))
    op.create_foreign_key('product_ibfk_2', 'product', 'product_type', ['id_product_type'], ['id_product_type'])
    op.drop_column('product', 'discount')
    op.drop_column('product', 'image')
    op.drop_column('product', 'product_type')
    op.drop_column('product', 'name')
    # ### end Alembic commands ###
