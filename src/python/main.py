from flask import Flask, stream_with_context, request, Response
from datetime import datetime
import time

app = Flask(__name__)

@app.route("/streams")
def stream():
    def event_stream():
        while True:
            time.sleep( 5 )
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            yield "data: {}\n\n".format(current_time)
    
    return Response(event_stream(), mimetype="text/event-stream")

@app.route('/stream')
def streamed_response():
    def generate():
        yield 'Hello '
        yield request.args['name']
        yield '!'
    return Response(stream_with_context(generate()), mimetype="text/event-stream")

@app.route('/')
def hello_world():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return 'Hello, World {}'.format(current_time)

def main():
    app.run(host='0.0.0.0', port=9876)

if __name__ == '__main__':
    main()