"""add projects and timeline fields

Revision ID: d9a1c4e55b11
Revises: ca0f61ca0ef0
Create Date: 2026-03-08 14:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "d9a1c4e55b11"
down_revision: Union[str, Sequence[str], None] = "ca0f61ca0ef0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    from sqlalchemy.engine.reflection import Inspector

    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()

    if "projects" not in tables:
        op.create_table(
            "projects",
            sa.Column("id", sa.Integer(), nullable=False),
            sa.Column("user_id", sa.Integer(), nullable=False),
            sa.Column("name", sa.String(), nullable=False),
            sa.Column("description", sa.String(), nullable=True),
            sa.Column("color", sa.String(), nullable=True),
            sa.Column("icon", sa.String(), nullable=True),
            sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=True),
            sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
            sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
            sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
            sa.PrimaryKeyConstraint("id"),
        )
        op.create_index(op.f("ix_projects_id"), "projects", ["id"], unique=False)
        op.create_index(op.f("ix_projects_name"), "projects", ["name"], unique=False)
        op.create_index(op.f("ix_projects_user_id"), "projects", ["user_id"], unique=False)

    mem_cols = {c["name"] for c in inspector.get_columns("memories")}

    if "project_id" not in mem_cols:
        op.add_column("memories", sa.Column("project_id", sa.Integer(), nullable=True))
        op.create_index(op.f("ix_memories_project_id"), "memories", ["project_id"], unique=False)
        op.create_foreign_key(None, "memories", "projects", ["project_id"], ["id"])

    if "source_app" not in mem_cols:
        op.add_column("memories", sa.Column("source_app", sa.String(), nullable=True))

    if "interaction_type" not in mem_cols:
        op.add_column("memories", sa.Column("interaction_type", sa.String(), nullable=True))


def downgrade() -> None:
    conn = op.get_bind()
    from sqlalchemy.engine.reflection import Inspector

    inspector = Inspector.from_engine(conn)

    mem_cols = {c["name"] for c in inspector.get_columns("memories")}
    if "interaction_type" in mem_cols:
        op.drop_column("memories", "interaction_type")
    if "source_app" in mem_cols:
        op.drop_column("memories", "source_app")
    if "project_id" in mem_cols:
        fk_names = [fk["name"] for fk in inspector.get_foreign_keys("memories") if "project_id" in fk.get("constrained_columns", [])]
        for fk_name in fk_names:
            if fk_name:
                op.drop_constraint(fk_name, "memories", type_="foreignkey")
        idx = [i["name"] for i in inspector.get_indexes("memories") if i["name"] == op.f("ix_memories_project_id")]
        if idx:
            op.drop_index(op.f("ix_memories_project_id"), table_name="memories")
        op.drop_column("memories", "project_id")

    tables = inspector.get_table_names()
    if "projects" in tables:
        op.drop_index(op.f("ix_projects_user_id"), table_name="projects")
        op.drop_index(op.f("ix_projects_name"), table_name="projects")
        op.drop_index(op.f("ix_projects_id"), table_name="projects")
        op.drop_table("projects")
