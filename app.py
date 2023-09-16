
from flask import Flask, request
from controller.jobdesc_to_listskills import get_listskills_from_jobdesc
from controller.youtube_search import get_video_links_by_keyword
from controller.generate_project import generate_project_idea
from controller.youtube_search import  get_transcript

from util.response import  convert_to_json_resp
from config.config import Config

app = Flask(__name__)
app_config = Config()
app.config["openai_api_key"] = app_config.get_config_openai()
app.config["youtube_api_key"] = app_config.get_config_youtube_api()
app.config["openai_model"] = "gpt-4"

@app.route("/")
def hello_world():
    return  "hello world"

# search list of required skills from given job description
@app.route('/skills', methods=['POST'])
def skills():
    jobdesc = request.json['input']

    result = get_listskills_from_jobdesc(jobdesc, app.config)
    return convert_to_json_resp(result)

# search youtube video froma given keyword
@app.route('/search', methods=['POST'])
def search():
    keyword = request.json['input']
    result = get_video_links_by_keyword(keyword, app.config)
    return convert_to_json_resp(result)
    
# generate project idea from given skill and keypoints
@app.route('/project', methods=['POST'])
def project():
    skill = request.json['skill']
    keypoints = request.json['key_points']
    return convert_to_json_resp(generate_project_idea(skill, keypoints, app.config))


@app.route('/summary', methods=['POST'])
def summary():
    list_id = request.json['input']
    res = get_transcript(list_id, app.config)
    return convert_to_json_resp(res)