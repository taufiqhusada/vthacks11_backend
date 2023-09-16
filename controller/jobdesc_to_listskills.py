from config.openai_connector import init_openai_config

def get_listskills_from_jobdesc(content, config):

    openai = init_openai_config(config['openai_api_key'])

    prompt = f"""Your task is to list important technical skills based on the given job description delimited by triple backticks. 
                Make it short and separated for example 'C++\nJava\nBackend Development'  
                if the skills is long, just take the key points.  
                Job Description: ```{content}```"""

    response = openai.ChatCompletion.create(
    model=config['openai_model'],
    messages=[
        {
        "role": "user",
        "content": prompt
        },
    ],
    )

    response = response["choices"][0]["message"]["content"]
    # Try to print out the result
    return response.split('\n')