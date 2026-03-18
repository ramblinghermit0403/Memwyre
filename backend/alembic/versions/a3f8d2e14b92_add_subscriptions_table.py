"""Add subscriptions table

Revision ID: a3f8d2e14b92
Revises: 77d9b0593a71
Create Date: 2026-02-22 23:15:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3f8d2e14b92'
down_revision: Union[str, Sequence[str], None] = '77d9b0593a71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create subscriptions table for Dodo Payments integration."""
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    tables = inspector.get_table_names()

    if 'subscriptions' not in tables:
        op.create_table(
            'subscriptions',
            sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
            sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False, unique=True),
            sa.Column('dodo_subscription_id', sa.String(), nullable=True, unique=True),
            sa.Column('dodo_customer_id', sa.String(), nullable=True),
            sa.Column('status', sa.String(), server_default='inactive', nullable=False),
            sa.Column('plan', sa.String(), server_default='free', nullable=False),
            sa.Column('current_period_start', sa.DateTime(timezone=True), nullable=True),
            sa.Column('current_period_end', sa.DateTime(timezone=True), nullable=True),
            sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()')),
            sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        )

    inspector = sa.inspect(conn)
    indexes = {
        index['name']
        for index in inspector.get_indexes('subscriptions')
        if index.get('name')
    }
    unique_column_sets = {
        tuple(constraint.get('column_names') or [])
        for constraint in inspector.get_unique_constraints('subscriptions')
        if constraint.get('column_names')
    }
    unique_index_column_sets = {
        tuple(index.get('column_names') or [])
        for index in inspector.get_indexes('subscriptions')
        if index.get('unique') and index.get('column_names')
    }

    if (
        'ix_subscriptions_user_id' not in indexes
        and ('user_id',) not in unique_column_sets
        and ('user_id',) not in unique_index_column_sets
    ):
        op.create_index('ix_subscriptions_user_id', 'subscriptions', ['user_id'], unique=True)
    if (
        'ix_subscriptions_dodo_subscription_id' not in indexes
        and ('dodo_subscription_id',) not in unique_column_sets
        and ('dodo_subscription_id',) not in unique_index_column_sets
    ):
        op.create_index('ix_subscriptions_dodo_subscription_id', 'subscriptions', ['dodo_subscription_id'], unique=True)


def downgrade() -> None:
    """Drop subscriptions table."""
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    tables = inspector.get_table_names()

    if 'subscriptions' not in tables:
        return

    indexes = {
        index['name']
        for index in inspector.get_indexes('subscriptions')
        if index.get('name')
    }
    if 'ix_subscriptions_dodo_subscription_id' in indexes:
        op.drop_index('ix_subscriptions_dodo_subscription_id', table_name='subscriptions')
    if 'ix_subscriptions_user_id' in indexes:
        op.drop_index('ix_subscriptions_user_id', table_name='subscriptions')
    op.drop_table('subscriptions')
