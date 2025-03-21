"""made fields optionals

Revision ID: a68733ef4707
Revises: 6d5297fc8298
Create Date: 2024-11-18 14:07:21.221770

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a68733ef4707'
down_revision: Union[str, None] = '6d5297fc8298'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('estates', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('estates', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('estates', 'price',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('estates', 'owner_phone',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('estates', 'realtor_phone',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('estates', 'balcony_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('estates', 'condition_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('estates', 'district_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('estates', 'type_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('estates', 'room_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('estates', 'storey_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('estates', 'storey_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('estates', 'room_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('estates', 'type_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('estates', 'district_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('estates', 'condition_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('estates', 'balcony_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('estates', 'realtor_phone',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('estates', 'owner_phone',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('estates', 'price',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('estates', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('estates', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
