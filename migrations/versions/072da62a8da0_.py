"""empty message

Revision ID: 072da62a8da0
Revises: 9702c6369c8b
Create Date: 2023-08-29 18:11:03.195014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '072da62a8da0'
down_revision = '9702c6369c8b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('rotation_period', sa.String(length=250), nullable=False),
    sa.Column('orbital_period', sa.String(length=250), nullable=False),
    sa.Column('diameter', sa.String(length=250), nullable=False),
    sa.Column('climate', sa.String(length=250), nullable=False),
    sa.Column('gravity', sa.String(length=250), nullable=False),
    sa.Column('terrain', sa.String(length=250), nullable=False),
    sa.Column('superface_water', sa.String(length=250), nullable=False),
    sa.Column('population', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('apellido', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['apellido'])
        batch_op.create_unique_constraint(None, ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('apellido')
        batch_op.drop_column('name')

    op.drop_table('planets')
    # ### end Alembic commands ###