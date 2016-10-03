import json
import urllib.parse

import pytest
import flask

from api import api
from api.subparts.alpha import alpha
from api.subparts.beta import beta


@pytest.fixture
def client():
    app_instance = flask.Flask(__name__)
    app_instance.register_blueprint(api.api.blueprint)
    app_instance.register_blueprint(alpha.api.blueprint)
    app_instance.register_blueprint(beta.api.blueprint)
    app_instance.config['RESTPLUS_VALIDATE'] = True
    return app_instance.test_client()


def test_subpart_list(client):
    result = client.get('/subparts')
    assert [{'name': 'alpha', 'spec_path': '/subparts/alpha/spec'},
            {'name': 'beta', 'spec_path': '/subparts/beta/spec'}] == json.loads(result.data.decode('utf-8'))


def test_beta_versions(client):
    x = 'a'
    y = 'b'
    z = 5
    w = 12
    result_v1 = client.get('/subparts/beta/v1/betas?' + urllib.parse.urlencode(dict(x=x, y=y, z=z, w=w)))
    result_v2 = client.get('/subparts/beta/v2/betas?' + urllib.parse.urlencode(dict(x=x, y=y, z=z, w=w)))
    v2_expected_result = beta.get_a_beta(x, y, z, w)
    assert v2_expected_result != json.loads(result_v1.data.decode('utf-8'))
    assert v2_expected_result == json.loads(result_v2.data.decode('utf-8'))


def test_validation(client):
    result = client.get('/subparts/alpha/v1/alphas?x=a')
    assert 400 == result.status_code
    assert 'Input payload validation failed' in json.loads(result.data.decode('utf-8'))['message']
