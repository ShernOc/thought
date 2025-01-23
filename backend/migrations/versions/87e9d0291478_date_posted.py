"""date_posted 

Revision ID: 87e9d0291478
Revises: 658fe72cf947
Create Date: 2025-01-23 13:33:27.687495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87e9d0291478'
down_revision = '658fe72cf947'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blogs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_posted', sa.DateTime(), nullable=True))
        batch_op.drop_column('date_')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blogs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_', sa.DATETIME(), nullable=True))
        batch_op.drop_column('date_posted')

    # ### end Alembic commands ###
