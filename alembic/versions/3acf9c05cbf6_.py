"""empty message

Revision ID: 3acf9c05cbf6
Revises: 43203ca17614
Create Date: 2023-06-06 16:42:00.169996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3acf9c05cbf6'
down_revision = '43203ca17614'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hero', sa.Column('alter_ego', sa.String(length=24), nullable=True))
    op.add_column('hero', sa.Column('hero_power', sa.String(length=24), nullable=True))
    op.create_unique_constraint(None, 'hero', ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'hero', type_='unique')
    op.drop_column('hero', 'hero_power')
    op.drop_column('hero', 'alter_ego')
    # ### end Alembic commands ###