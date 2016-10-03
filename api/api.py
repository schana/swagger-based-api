import collections

import flask
import flask_restplus
from flask_restplus import fields

from api import util

api = util.build_api('api', __name__)

SubpartSpec = collections.namedtuple('Subpart', ['name', 'spec_path'])

subpart_model = api.model(SubpartSpec.__name__, SubpartSpec(
    name=fields.String(description='Name of the subpart'),
    spec_path=fields.String(description='Path to spec')
)._asdict())


@api.route('/subparts')
class Subpart(flask_restplus.Resource):

    @api.marshal_with(subpart_model, as_list=True)
    @api.doc(description='This returns the available subparts and the paths to their specs')
    def get(self):
        subparts = []
        for blue in flask.current_app.iter_blueprints():
            if type(blue) is flask.Blueprint and blue is not api.blueprint:
                subparts.append(SubpartSpec(
                    name=blue.name,
                    spec_path=flask.url_for(blue.name + '.spec')
                )._asdict())
        return subparts
