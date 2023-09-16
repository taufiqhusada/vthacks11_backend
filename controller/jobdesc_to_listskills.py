from config.openai_connector import init_openai_config

def get_listskills_from_jobdesc(content):
    openai = init_openai_config()

    prompt = f"""Can you help me list of important job skills from the given job desc delimited by triple backtick. 
                Make it short and separated for example 'C++\nJava\nBackend Development.' 
                if the skills is long, just take the key points.  ```{content}```"""

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "user",
        "content": prompt
        },
    ],
    )

    response = response["choices"][0]["message"]["content"]
    print(response)
    # Try to print out the result
    return response.split('\n')