import os


class Environment:
    DEV = 'dev'
    PROD = 'prod'

    URLS = {
        DEV: "https://playground.learnqa.ru/api_dev",
        PROD: "https://playground.learnqa.ru/api"
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except KeyError:
            self.env = self.DEV

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception (f"Unknown value of ENV variable {self.env}")

    def generate_environment_xml(self):
        with open("test_results/environment.xml", 'w', encoding='utf-8') as logger_file:
            logger_file.write\
                (f"<environment><parameter><key>Stand</key><value>{self.env}</value></parameter></environment>")

ENV_OBJECT = Environment()
Environment().generate_environment_xml()
