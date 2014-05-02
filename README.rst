=============
status_server
=============

Serve HTTP Status by URL

Quickstart
----------
1. ``pip install status_server``
2. ``status_server``
3. ``curl -i http://localhost:8888/200``

What is status_server?
----------------------
I was playing around with a load testing tool, and I wanted to generate more
than one HTTP response type, so I hacked this together.

status_server returns the status code in the request URI. Want a 200?
``curl http://localhost:8888/200``

Want a 404?
``curl http://localhost:8888/404``

What if you want a randomly chosen value from a list of possible return types?
``curl http://localhost:8888/200/404/503``

The above has an equal chance of returning either of the three HTTP status
codes. (1/3: 200, 1/3: 404, 1/3: 503)

status_server supports all standard methods for requests:

``curl -iX POST http://localhost:8888/200``

``curl -iX DELETE http://localhost:8888/200``

Known Issue
-----------
304 (Not Modified) does **not** work. ``curl http://localhost:8888/304`` will
throw an exception and return a 500, not a 304.
