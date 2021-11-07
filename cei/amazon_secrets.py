import os

class AmazonSecrets:
    accessKey = ""
    secretKey = ""
    def __init__(self) -> None:
        self.accessKey = os.environ['AMAZON_ACCESS_KEY_ADRIANO']
        self.secretKey = os.environ['AMAZON_SECRET_KEY_ADRIANO']
        pass