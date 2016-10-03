import collections

import flask_restplus
from flask_restplus import fields
from flask_restplus import reqparse

from api import util

api = util.build_api('alpha', __name__, url_prefix='/subparts/alpha')
v1 = util.build_namespace(api, 'v1', description='Version 1')

AlphaSpec = collections.namedtuple('Alpha', ['x_and_y', 'z'])

alpha_model = v1.model(AlphaSpec.__name__, AlphaSpec(
    x_and_y=fields.Integer(description='x plus y', required=True),
    z=fields.String(description='z-e-d', required=True)
)._asdict())

alpha_params = reqparse.RequestParser()
alpha_params.add_argument('x', type=int, required=True)
alpha_params.add_argument('y', type=int, required=False, default=0)
alpha_params.add_argument('z', type=str, required=True)


@v1.route('/alphas')
class Alpha(flask_restplus.Resource):

    @v1.expect(alpha_params)
    @v1.marshal_with(alpha_model)
    @v1.doc(description='A super-helpful description as to what is going on',
            params={'x': 'The best x of them all'})
    def get(self):
        args = alpha_params.parse_args()
        return AlphaSpec(x_and_y=args['x'] + args['y'],
                         z=args['z'])._asdict()
