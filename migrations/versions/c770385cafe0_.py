"""empty message

Revision ID: c770385cafe0
Revises: 7c5c235b5a4e
Create Date: 2020-11-01 13:31:00.529355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c770385cafe0'
down_revision = '7c5c235b5a4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('auth', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('auth', sa.Column('is_active', sa.Boolean(), nullable=True))
    op.add_column('standup', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'created_at')
    op.drop_column('standup', 'created_at')
    op.drop_column('auth', 'is_active')
    op.drop_column('auth', 'created_at')
    # ### end Alembic commands ###
