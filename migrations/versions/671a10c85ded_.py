"""empty message

Revision ID: 671a10c85ded
Revises: 345ecc3039f3
Create Date: 2024-07-12 22:26:48.849397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '671a10c85ded'
down_revision = '345ecc3039f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite_movie', schema=None) as batch_op:
        batch_op.add_column(sa.Column('media_type', sa.String(length=80), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite_movie', schema=None) as batch_op:
        batch_op.drop_column('media_type')

    # ### end Alembic commands ###
