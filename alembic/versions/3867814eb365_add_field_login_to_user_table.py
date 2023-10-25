"""Add_field_login_to_user_table

Revision ID: 3867814eb365
Revises: 8030a94084b1
Create Date: 2023-10-23 21:16:04.950102

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3867814eb365'
down_revision: Union[str, None] = '8030a94084b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('login', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'login')
    # ### end Alembic commands ###