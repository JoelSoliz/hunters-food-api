"""we add a new field to business

Revision ID: 1f0352ca0cd1
Revises: 442753fd4f78
Create Date: 2022-10-16 19:36:19.483496

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1f0352ca0cd1'
down_revision = '442753fd4f78'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('business', sa.Column('name', sa.String(length=50), nullable=False))
    op.add_column('business', sa.Column('logo', sa.BLOB(), nullable=False))
    op.add_column('business', sa.Column('description', sa.String(length=256), nullable=False))
    op.drop_column('business', 'image_logo')
    op.drop_column('business', 'name_business')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('business', sa.Column('name_business', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('business', sa.Column('image_logo', mysql.LONGBLOB(), nullable=False))
    op.drop_column('business', 'description')
    op.drop_column('business', 'logo')
    op.drop_column('business', 'name')
    # ### end Alembic commands ###
