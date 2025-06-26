"""test2

Revision ID: e051c71326d2
Revises: 250401a4934d
Create Date: 2025-06-19 19:36:04.742848

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e051c71326d2'
down_revision: Union[str, Sequence[str], None] = '250401a4934d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
