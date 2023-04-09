"""initial migration

Revision ID: ca322453f0c8
Revises: 
Create Date: 2023-04-08 22:31:27.231585

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Enum

# revision identifiers, used by Alembic.
revision = 'ca322453f0c8'
down_revision = None
branch_labels = None
depends_on = None


# Define the upgrade and downgrade functions for this migration
def upgrade():
    op.create_table(
        "office",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String(30), nullable=False, unique=True),
    )
    
    op.create_table(
        "person",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String(50), nullable=False, unique=True),
        sa.Column("age", sa.Integer, nullable=False),
        sa.Column("is_retired", sa.Boolean, nullable=False),
        sa.Column("nationality", Enum('br', 'en', 'ar', name='nationality'), nullable=False),
        sa.Column("id_office", sa.Integer, sa.ForeignKey("office.id"), nullable=False),
    )

def downgrade():
    op.drop_table("person")
    op.drop_table("office")
