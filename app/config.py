import os

class Config:


    SECRET_KEY = 'yes'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Bryon:nayere@localhost/pizza_shop'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
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

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Bryon:nayere@localhost/pizza_shop'
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Bryon:nayere@localhost/pizza_shop_test'



config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}