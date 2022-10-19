"""change-model

Revision ID: 1f04e5190919
Revises: 776e2d86a22f
Create Date: 2022-10-15 20:51:17.898823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f04e5190919'
down_revision = '776e2d86a22f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('business', 'image_logo')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('business', sa.Column('image_logo', sa.BLOB(), nullable=False))
    # ### end Alembic commands ###