"""test migration for downgrade

Revision ID: 250401a4934d
Revises: 2ddec31e45aa
Create Date: 2025-06-19 19:29:14.913027

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '250401a4934d'
down_revision: Union[str, Sequence[str], None] = '2ddec31e45aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
