"""Add email verification tokens

Revision ID: ca0f61ca0ef0
Revises: 3d674e6c6e2a
Create Date: 2026-03-04 12:17:45.074689

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca0f61ca0ef0'
down_revision: Union[str, Sequence[str], None] = '3d674e6c6e2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    conn = op.get_bind()
    from sqlalchemy.engine.reflection import Inspector
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    
    if 'verification_tokens' not in tables:
        op.create_table('verification_tokens',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('token', sa.String(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('token_type', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
        )
        op.create_index(op.f('ix_verification_tokens_id'), 'verification_tokens', ['id'], unique=False)
        op.create_index(op.f('ix_verification_tokens_token'), 'verification_tokens', ['token'], unique=True)
        
    cols = [c['name'] for c in inspector.get_columns('users')]
    if 'is_verified' not in cols:
        op.add_column('users', sa.Column('is_verified', sa.Boolean(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    conn = op.get_bind()
    from sqlalchemy.engine.reflection import Inspector
    inspector = Inspector.from_engine(conn)
    
    cols = [c['name'] for c in inspector.get_columns('users')]
    if 'is_verified' in cols:
        op.drop_column('users', 'is_verified')
        
    tables = inspector.get_table_names()
    if 'verification_tokens' in tables:
        op.drop_index(op.f('ix_verification_tokens_token'), table_name='verification_tokens')
        op.drop_index(op.f('ix_verification_tokens_id'), table_name='verification_tokens')
        op.drop_table('verification_tokens')
