"""empty message

Revision ID: 88af94edd37d
Revises: c0655130bd5d
Create Date: 2021-05-22 13:23:00.820035

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88af94edd37d'
down_revision = 'c0655130bd5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('videos_checked_out_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'videos_checked_out_count')
    # ### end Alembic commands ###