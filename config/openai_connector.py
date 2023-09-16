import os
import openai

def init_openai_config(api_key):
    # please insert your openai key here
    openai.api_key = api_key
    # Try to print out the result
    return openai