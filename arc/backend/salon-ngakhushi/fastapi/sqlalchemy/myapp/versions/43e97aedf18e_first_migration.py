"""first migration

Revision ID: 43e97aedf18e
Revises: 
Create Date: 2025-06-19 19:11:47.414581

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43e97aedf18e'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "test_table",        
        sa.Column("task_no", sa.Integer, primary_key= True, index= True, nullable= False),
        sa.Column("task", sa.String(100), nullable= False, index= True),
        sa.Column("day", sa.Integer, sa.ForeignKey("tasks.day"), index= True)
    )


def downgrade() -> None:
    op.drop_table("test_table")
