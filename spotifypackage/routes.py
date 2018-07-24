from flask import render_template, jsonify, json
from spotifypackage.models import *
from spotifypackage import *
from spotifypackage.dashboard import app

@app.server.route('/conclusions')
def findings():
   return render_template('conclusions.html')
