from flask import Flask, jsonify, request
from youtube_transcript_api import YouTubeTranscriptApi
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route("/<string:id>")
def sub(id):
  sub = YouTubeTranscriptApi.get_transcript(id)
  _list = [x['text'] for x in sub]
  s = " ".join(_list)
  if len(id) == 0:
    abort(400)
  try:
    return jsonify({"sub": s})
  except:
    return jsonify({"msg":"Transcribe is disabled for requested youtube video"})

if __name__ == "__main__":
    app.run()
