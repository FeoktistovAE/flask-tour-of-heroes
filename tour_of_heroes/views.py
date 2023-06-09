from flask_restful import Resource
from flask import request

from tour_of_heroes.models import Hero, HeroSchema
from tour_of_heroes.spec import get_apispec
from tour_of_heroes.config import db, app
import json


class Heroes(Resource):
    def get(self):
        """Returns all heroes.
        ---
        """
        heroes = db.session.execute(db.select(Hero).order_by(Hero.name)).scalars()
        heroses_schema = HeroSchema(many=True)
        return heroses_schema.dump(heroes)


class AddHero(Resource):
    def post(self):
        """Adds a hero by an ID.
        ---
        """
        hero = Hero(
            name=request.form['name'],
            alter_ego=request.form['alter_ego'],
            hero_power=request.form['hero_power'],
        )
        db.session.add(hero)
        db.session.commit()
        return {'success': f"Hero '{hero.name}' successfully added"}


class RemoveHero(Resource):
    def post(self, id):
        hero = db.get_or_404(Hero, id)
        db.session.delete(hero)
        db.session.commit()
        return {'success': f"Hero '{hero.name}' succesfully deleted"}


class DetailHero(Resource):
    def get(self, id):
        hero = db.get_or_404(Hero, id)
        hero_schema = HeroSchema()
        return hero_schema.dump(hero)


class UpdateHero(Resource):
    def post(self, id):
        hero = Hero.query.get(id)
        hero.name = request.form['name'],
        hero.alter_ego = request.form['alter_ego']
        hero.hero_power = request.form['hero_power']
        db.session.commit()
        return {'success': f"Hero '{hero.name}' succesfully updated"}


class SearchHero(Resource):
    def get(self, name):
        hero = db.one_or_404(
            db.select(Hero).filter_by(name=name),
            description=f"No hero named '{name}'."
        )
        hero_schema = HeroSchema()
        return hero_schema.dump(hero)


@app.route('/swagger')
def create_swagger_spec():
    return json.dumps(get_apispec(app).to_dict())
