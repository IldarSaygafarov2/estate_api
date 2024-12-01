"""added fixes to estate model

Revision ID: ad359113c7c1
Revises: a0a79b5398a4
Create Date: 2024-12-01 02:37:08.788916

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'ad359113c7c1'
down_revision: Union[str, None] = 'a0a79b5398a4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # ### commands auto generated by Alembic - please adjust! ###
    # op.alter_column('estates', 'price',
    #                 existing_type=sa.VARCHAR(),
    #                 type_=sa.Integer(),
    #                 existing_nullable=True,
    #                 using=sa.Integer())

    op.execute("ALTER TABLE estates ALTER COLUMN price TYPE INTEGER USING price::integer")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('estates', 'price',
                    existing_type=sa.Integer(),
                    type_=sa.VARCHAR(),
                    existing_nullable=True)
    # ### end Alembic commands ###