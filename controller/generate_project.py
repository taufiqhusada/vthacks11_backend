from config.openai_connector import init_openai_config

def generate_project_idea(skill, key_points, config):
    openai = init_openai_config(config['openai_api_key'])

    prompt = f"""Your task is to generate project idea to showcase skills in {skill} for beginner 
                and generate a boilerplate code for the project too and also create step by step to setup the project too.
                the project ide must be clear and should list the features that I need to implement. The boilerplate code must be clear and give enough guidance
                
                This project must based on key points provided in the key learning materials delimited by triple backticks
                Learning Materials: ```{key_points}```
                """

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
    return response