from flask import Flask
from redis import Redis
import os
import requests

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/hits')
def hits():
    redis.incr('hits')
    return 'Number of hits: %s' % redis.get('hits')

@app.route('/google')
def google():	
    return requests.get('http://www.google.com').content

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
