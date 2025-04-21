"""create transactions table

Revision ID: 0001
Revises: 
Create Date: 2025-04-21 23:23:00.000000

"""
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as pg

def upgrade():
    op.create_table(
        'transactions',
        sa.Column('id', pg.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column('date', sa.Date, nullable=False),
        sa.Column('description', sa.String, nullable=False),
        sa.Column('amount', sa.Numeric(12, 2), nullable=False),
    )

def downgrade():
    op.drop_table('transactions')
