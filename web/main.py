import os
from flask import Flask, render_template, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from llama_index import StorageContext, load_index_from_storage

import openai
openai.api_key = os.getenv("OPENAI_API_KEY")


app = Flask(__name__)
limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["100 per minute"],
        storage_uri=os.getenv("FLASK_LIMITER_STORAGE_URI")
)

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="./storage")
# load index
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()

@app.route("/")
def routing_index():
    return render_template("main.html")

@app.route("/help")
def routing_help():
    return render_template("help.html")

@app.route("/limitcheck")
@limiter.limit("5 per minute")
def routing_limitcheck():
    return "ok"

@app.route("/api/search", methods=["POST"])
@limiter.limit("100 per day")
def routing_apiSearch():
    req = request.get_json()
    query = req['query']
    if (query == ""):
        return {"error": "need query parameter"}, 400

    response = openai.Completion.create(
        prompt= "Translate to English: " + req['query'],
        model="text-davinci-003"
    )
    queryEnglish = response["choices"][0]["text"].strip().strip("Title").strip("タイトル").strip(":").strip()

    response = query_engine.query(queryEnglish)

    return {"llama_index_response": response}
