import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())
config = dotenv.dotenv_values(dotenv.find_dotenv())


class Config(object):
    # Flask
    FLASK_APP = config.get("FLASK_APP") or "app.py"
    FLASK_DEBUG = config.get("FLASK_DEBUG") or False

    # Google Cloud API Credentials
    GOOGLE_APPLICATION_CREDENTIALS = (
        config.get("GOOGLE_APPLICATION_CREDENTIALS")
        or "application_default_credentials.json"
    )
