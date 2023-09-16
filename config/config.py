import configparser

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config/config.ini")

    def get_config_openai(self):
        print(self.config)
        return self.config['credentials']['openai_api_key']
    
    def get_config_youtube_api(self):
        return self.config['credentials']['youtube_api_key']