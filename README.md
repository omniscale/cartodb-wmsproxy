WMSProxy
========

WMSProxy is a proxy that makes CartoDB user layers available as WMS and WMTS.
WMTProxy does this by creating MapProxy configurations based on the viz.json for a user. Configurations are created dynamically and are cached for a few minutes.

See example_config.py for an example WSGI configuration.

The WMS is available at: http://localhost/<username>/service?

The WMTS is available at: http://localhost/<username>/wmts/1.0.0/WMTSCapabilities.xml