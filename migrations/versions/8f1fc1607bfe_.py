"""empty message

Revision ID: 8f1fc1607bfe
Revises: 95289e66eb98
Create Date: 2023-11-24 16:33:29.683724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f1fc1607bfe'
down_revision = '95289e66eb98'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('quand', sa.String(length=255), nullable=False))
        batch_op.create_index(batch_op.f('ix_Task_quand'), ['quand'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Task', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Task_quand'))
        batch_op.drop_column('quand')

    # ### end Alembic commands ###
