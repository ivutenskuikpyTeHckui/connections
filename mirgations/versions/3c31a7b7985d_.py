"""empty message

Revision ID: 3c31a7b7985d
Revises: 5e3631e7fdf9
Create Date: 2024-06-16 18:11:13.580485

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c31a7b7985d'
down_revision: Union[str, None] = '5e3631e7fdf9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('connect',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('profession', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('info', sa.String(), nullable=True),
    sa.Column('master_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('connect')
    # ### end Alembic commands ###