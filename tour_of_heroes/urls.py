from tour_of_heroes.config import api
from tour_of_heroes.views import Heroes, AddHero, RemoveHero, \
    DetailHero, UpdateHero, SearchHero


api.add_resource(Heroes,
                 '/',
                 '/heroes')
api.add_resource(AddHero, '/hero/create')
api.add_resource(RemoveHero, '/hero/<int:id>/delete')
api.add_resource(DetailHero, '/hero/<int:id>/detail')
api.add_resource(UpdateHero, '/hero/<int:id>/update')
api.add_resource(SearchHero, '/hero/<string:name>/search')
