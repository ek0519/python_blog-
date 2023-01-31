"""add root_cause table

Revision ID: 5634be8910c8
Revises: 
Create Date: 2023-01-25 16:33:47.364878

"""
import datetime

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5634be8910c8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'blogs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('created_at', sa.TIMESTAMP(), default=datetime.datetime.utcnow),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('cover', sa.String(255), nullable=False),
        sa.Column('content', sa.TEXT(), nullable=False),
    )


def downgrade():
    op.drop_table('blogs')
