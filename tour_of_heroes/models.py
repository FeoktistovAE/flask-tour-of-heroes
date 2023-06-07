from tour_of_heroes.config import db, ma


class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), nullable=False, unique=True)
    alter_ego = db.Column(db.String(24))
    hero_power = db.Column(db.String(24), nullable=False)


class HeroSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'alter_ego', 'hero_power')
