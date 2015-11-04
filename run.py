#!flask/bin/python
import os, sys
""" start the server """

# import app variable from our app package
from app import app
app.run(host='0.0.0.0', debug=True)
