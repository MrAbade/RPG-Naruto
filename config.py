class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    env = 'development'
    SQLALCHEMY_DATABASE_URI = 'postgresql://mrabade:pain321123@localhost:5432/Naruto'
    

class ProductionConfig(Config):
    ...


class TestConfig(Config):
    ...


config_selector = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'production': ProductionConfig
}
