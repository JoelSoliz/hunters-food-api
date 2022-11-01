"""product description increased

Revision ID: acc9350e8884
Revises: 640b3ebfe1a0
Create Date: 2022-10-27 22:54:48.578403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acc9350e8884'
down_revision = '640b3ebfe1a0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('description', sa.String(length=256), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'description')
    # ### end Alembic commands ###
