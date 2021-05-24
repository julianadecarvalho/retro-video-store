"""empty message

Revision ID: 9bb7550db773
Revises: 88af94edd37d
Create Date: 2021-05-22 13:42:33.839439

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9bb7550db773'
down_revision = '88af94edd37d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('videos',
    sa.Column('video_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('release_date', sa.DateTime(), nullable=True),
    sa.Column('total_inventory', sa.Integer(), nullable=True),
    sa.Column('available_inventory', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('video_id')
    )
    op.drop_table('video')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('video',
    sa.Column('video_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('release_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('total_inventory', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('available_inventory', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('video_id', name='video_pkey')
    )
    op.drop_table('videos')
    # ### end Alembic commands ###