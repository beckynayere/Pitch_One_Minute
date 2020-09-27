import os

class Config:


    SECRET_KEY = 'yes'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Bryon:nayere@localhost/pitch_minute'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/images'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


    #email configurations
    MAIL_SERVER ='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD =os.environ.get("MAIL_PASSWORD")

    


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Bryon:nayere@localhost/pitch_minute'
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Bryon:nayere@localhost/pitch_minute_test'



config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}