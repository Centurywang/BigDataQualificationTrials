import os

base_dir = os.path.abspath(os.path.dirname(__file__))


# 通用配置
class Config:
    # 秘钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    # 数据库
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 额外的初始化操作，即使什么内容都没有写，也是有意义的
    @staticmethod
    def init_app(app):
        pass


# 开发环境
class DevelopmentConfig(Config):



# 测试环境
class TestingConfig(Config):



# 生产环境
class ProductionConfig(Config):



# 配置字典
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
