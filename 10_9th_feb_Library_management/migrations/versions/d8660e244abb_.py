"""empty message

Revision ID: d8660e244abb
Revises: 
Create Date: 2023-02-13 16:00:21.572763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8660e244abb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('book_name', sa.String(length=50), nullable=False),
    sa.Column('book_author', sa.String(length=50), nullable=False),
    sa.Column('book_stock', sa.Integer(), nullable=False),
    sa.Column('votes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('book_id')
    )
    op.create_table('members',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=10), nullable=False),
    sa.Column('debt', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('transactions',
    sa.Column('tra_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.Column('book_name', sa.String(length=50), nullable=False),
    sa.Column('from_date', sa.Date(), nullable=False),
    sa.Column('borrowed', sa.Boolean(), nullable=False),
    sa.Column('fine', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('tra_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('members')
    op.drop_table('books')
    # ### end Alembic commands ###
