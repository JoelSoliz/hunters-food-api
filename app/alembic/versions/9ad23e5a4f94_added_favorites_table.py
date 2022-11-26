"""added favorites table

Revision ID: 9ad23e5a4f94
Revises: 6e5d9127ca6e
Create Date: 2022-11-22 21:47:40.292792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ad23e5a4f94'
down_revision = '6e5d9127ca6e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite',
    sa.Column('id_favorite', sa.String(length=4), nullable=False),
    sa.Column('id_business', sa.String(length=4), nullable=True),
    sa.Column('id_user', sa.String(length=4), nullable=True),
    sa.ForeignKeyConstraint(['id_business'], ['business.id_business'], ),
    sa.ForeignKeyConstraint(['id_user'], ['user.id_user'], ),
    sa.PrimaryKeyConstraint('id_favorite')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    # ### end Alembic commands ###