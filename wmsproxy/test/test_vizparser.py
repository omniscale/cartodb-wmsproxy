import httpretty
from wmsproxy.viz import tile_params, RequestError

import os.path

from nose.tools import eq_, assert_raises

@httpretty.activate
def test_tile_params():
    viz_url = 'http://osm2.cartodb.com/api/v2/viz/fda70aae-a7a5-11e4-96f0-0e0c41326911/viz.json'
    httpretty.register_uri('GET', viz_url,
        body=open(os.path.join(os.path.dirname(__file__), 'test-vis.json')).read())

    # tiler_url

    def tiler_req(request, uri, headers):
        eq_(request.headers['Content-type'], 'application/json')
        return (200, headers, open(os.path.join(os.path.dirname(__file__), 'test-tiler-resp.json')).read())

    httpretty.register_uri('POST', 'http://osm2.cartodb.com:80/api/v1/map',
        body=tiler_req)

    params = tile_params('osm2', 'fda70aae-a7a5-11e4-96f0-0e0c41326911')
    eq_(params['url'], 'http://0.ashbu.cartocdn.com/osm2/api/v1/map/235546e1476036314c850900596b4415:1422529684709.27/')
    eq_(params['bounds'], [-71.2369179725647, 42.66377193433536, -71.2114691734314, 42.67511582354274])
    eq_(params['title'], 'spencer')



@httpretty.activate
def test_tile_params_viz_error():
    viz_url = 'http://osm2.cartodb.com/api/v2/viz/fda70aae-a7a5-11e4-96f0-0e0c41326911/viz.json'
    httpretty.register_uri('GET', viz_url,
        body='{"error": true}', status=500)
    assert_raises(RequestError, tile_params, 'osm2', 'fda70aae-a7a5-11e4-96f0-0e0c41326911')

