# vote/app.py

from flask import Flask, request
import redis

app = Flask(__name__)

r = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def index():
    return "Voting App is running!"

@app.route('/vote', methods=['POST'])
def vote():
    vote = request.form['vote']
    r.lpush('votes', vote)
    return f"Vote for {vote} received!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
