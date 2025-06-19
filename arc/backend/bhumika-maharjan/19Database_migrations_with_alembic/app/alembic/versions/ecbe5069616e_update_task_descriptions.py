"""Update task descriptions

Revision ID: ecbe5069616e
Revises: c0a9cb531f70
Create Date: 2025-06-18 18:56:27.881676

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecbe5069616e'
down_revision: Union[str, Sequence[str], None] = 'c0a9cb531f70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



# def upgrade() -> None:
#     """Upgrade schema."""
#     pass

from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

task_table = table('tasks',
    column('id', Integer),
    column('description', String)
)

def upgrade():
    op.execute(
        task_table.update().where(task_table.c.description == None)
        .values(description="No description")
    )



def downgrade() -> None:
    """Downgrade schema."""
    pass
