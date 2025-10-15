"""add events table

Revision ID: 0002_events
Revises: 0001_init
Create Date: 2025-10-14 11:31:47

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0002_events'
down_revision = '0001_init'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('events',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(length=200), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
        sa.Column('academicGroupId', sa.String(length=50), nullable=True),
        sa.Column('eventType', sa.String(length=50), nullable=True, server_default='evento-geral'),
        sa.Column('creatorId', sa.Integer(), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'))
    )
    op.create_index('idx_event_timestamp', 'events', ['timestamp'])
    op.create_index('idx_event_creator', 'events', ['creatorId'])

def downgrade():
    op.drop_index('idx_event_timestamp', table_name='events')
    op.drop_index('idx_event_creator', table_name='events')
    op.drop_table('events')
