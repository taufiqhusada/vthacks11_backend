
from flask import Flask, request
from controller.jobdesc_to_listskills import get_listskills_from_jobdesc
from util.response import  convert_to_json_resp

app = Flask(__name__)

@app.route("/")
def hello_world():
    return  "hello world"

@app.route('/skills', methods=['POST'])
def skills():
    jobdesc = request.json['input']

    result = get_listskills_from_jobdesc(jobdesc)
    return convert_to_json_resp(result)
    