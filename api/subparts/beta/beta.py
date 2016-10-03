import flask_restplus
from flask_restplus import fields
from flask_restplus import reqparse

from api import util

api = util.build_api('beta', __name__, url_prefix='/subparts/beta')
v1 = util.build_namespace(api, 'v1', description='Version 1')

beta_model = v1.model('Beta', dict(
    x_concat_y=fields.String(description='x concat y', required=True),
    z=fields.Integer(description='z-e-d', required=True)
))

beta_params = reqparse.RequestParser()
beta_params.add_argument('x', type=str, required=True)
beta_params.add_argument('y', type=str, required=False, default='')
beta_params.add_argument('z', type=int, required=True)


@v1.route('/betas')
class Beta(flask_restplus.Resource):

    @v1.expect(beta_params)
    @v1.marshal_with(beta_model)
    def get(self):
        args = beta_params.parse_args()
        return get_a_beta(args['x'], args['y'], args['z'])


v2 = util.build_namespace(api, 'v2', description='Version 2')
beta_model_v2 = v1.clone('Beta_v2', beta_model, dict(
    z_times_w=fields.Integer(description='z times w', required=True)
))
beta_params_v2 = beta_params.copy()
beta_params_v2.add_argument('w', type=int, required=False, default=1)


@v2.route('/betas')
class BetaV2(flask_restplus.Resource):

    @v2.expect(beta_params_v2)
    @v2.marshal_with(beta_model_v2)
    def get(self):
        args = beta_params_v2.parse_args()
        return get_a_beta(args['x'], args['y'], args['z'], args['w'])


def get_a_beta(x, y, z, w=1):
    return dict(x_concat_y=x + y,
                z=z,
                z_times_w=z * w)
