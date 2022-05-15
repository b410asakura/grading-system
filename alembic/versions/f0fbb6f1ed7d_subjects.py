"""subjects

Revision ID: f0fbb6f1ed7d
Revises: 284debb1a8c9
Create Date: 2022-05-15 18:27:51.255433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0fbb6f1ed7d'
down_revision = '284debb1a8c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('register_subject', sa.Column('mid_grade', sa.Integer(), nullable=True))
    op.add_column('register_subject', sa.Column('mid_average', sa.Integer(), nullable=True))
    op.add_column('register_subject', sa.Column('fin_grade', sa.Integer(), nullable=True))
    op.add_column('register_subject', sa.Column('fin_average', sa.Integer(), nullable=True))
    op.add_column('register_subject', sa.Column('total', sa.Integer(), nullable=True))
    op.drop_column('subject', 'mid_grade')
    op.drop_column('subject', 'total')
    op.drop_column('subject', 'fin_average')
    op.drop_column('subject', 'fin_grade')
    op.drop_column('subject', 'mid_average')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subject', sa.Column('mid_average', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('subject', sa.Column('fin_grade', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('subject', sa.Column('fin_average', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('subject', sa.Column('total', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('subject', sa.Column('mid_grade', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('register_subject', 'total')
    op.drop_column('register_subject', 'fin_average')
    op.drop_column('register_subject', 'fin_grade')
    op.drop_column('register_subject', 'mid_average')
    op.drop_column('register_subject', 'mid_grade')
    # ### end Alembic commands ###
