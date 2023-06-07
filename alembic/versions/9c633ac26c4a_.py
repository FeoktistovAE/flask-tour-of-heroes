"""empty message

Revision ID: 9c633ac26c4a
Revises: 3acf9c05cbf6
Create Date: 2023-06-06 20:52:39.959679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c633ac26c4a'
down_revision = '3acf9c05cbf6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('hero', 'hero_power',
               existing_type=sa.VARCHAR(length=24),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('hero', 'hero_power',
               existing_type=sa.VARCHAR(length=24),
               nullable=True)
    # ### end Alembic commands ###
