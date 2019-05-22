"""empty message

Revision ID: b076d1cc461a
Revises: 38aa8ac3902e
Create Date: 2019-05-05 23:04:44.906524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b076d1cc461a'
down_revision = '38aa8ac3902e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("opportunity") as batch_op:
        batch_op.add_column(sa.Column('frequency_modifier', sa.String(length=5), nullable=True))
        batch_op.add_column(sa.Column('frequency_unit', sa.String(length=25), nullable=True))
        batch_op.drop_column('frequency_id')
    op.drop_table('frequency')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("opportunity") as batch_op:
        batch_op.add_column(sa.Column('frequency_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('opportunity_frequency_id_fkey', 'frequency', ['frequency_id'], ['id'])
        batch_op.drop_column('frequency_unit')
        batch_op.drop_column('frequency_modifier')
    op.create_table('frequency',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='frequency_pkey')
    )
    op.create_index('ix_frequency_name', 'frequency', ['name'], unique=True)
    op.create_index('ix_frequency_id', 'frequency', ['id'], unique=False)
    # ### end Alembic commands ###
