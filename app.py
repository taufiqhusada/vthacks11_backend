
from flask import Flask, request
from controller.jobdesc_to_listskills import get_listskills_from_jobdesc
from util.response import  convert_to_json_resp
from config.config import Config

app = Flask(__name__)
app_config = Config()
app.config["openai_api_key"] = app_config.get_config_openai()
app.config["youtube_api_key"] = app_config.get_config_youtube_api()
app.config["openai_model"] = "gpt-3.5-turbo"

@app.route("/")
def hello_world():
    return  "hello world"

@app.route('/skills', methods=['POST'])
def skills():
    jobdesc = request.json['input']

    result = get_listskills_from_jobdesc(jobdesc, app.config)
    return convert_to_json_resp(result)
    