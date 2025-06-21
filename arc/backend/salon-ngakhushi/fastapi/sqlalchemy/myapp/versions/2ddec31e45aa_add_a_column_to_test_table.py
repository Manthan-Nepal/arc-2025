"""add a column to test_table

Revision ID: 2ddec31e45aa
Revises: 43e97aedf18e
Create Date: 2025-06-19 19:22:37.128442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ddec31e45aa'
down_revision: Union[str, Sequence[str], None] = '43e97aedf18e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "test_table",
        sa.Column("test_column", sa.String(20), nullable= False)
    )


def downgrade() -> None:
    op.drop_column("test_table", "test_column")
