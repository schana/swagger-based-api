import flask
import flask_restplus as restplus


def build_api(name, import_name, url_prefix=None):
    blueprint = flask.Blueprint(name, import_name, url_prefix=url_prefix)
    api = restplus.Api(blueprint)

    class Spec(restplus.Resource):
        def get(self):
            return flask.jsonify(api.__schema__)

    api.add_resource(Spec, '/spec')
    return api


def build_namespace(api, name, description):
    return api.namespace(name, description=description)
