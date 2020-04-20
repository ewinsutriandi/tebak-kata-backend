import application
class BaseConfig(object):
    DEBUG = True
    TESTING = False
    SECRET_KEY = '?'
    DBHOST = 'localhost'
    DBUSER = 'root'
    DBPASS = 'root'
    DBNAME = 'wg'
    #CORS_ORIGINS= ['http://localhost:8080','https://sidatu.lomboktengahkab.go.id']
    #UPLOAD_FOLDER = str(os.path.dirname(os.path.abspath(__file__))+'/static/image')
    #UPLOAD_MAX_CTN_LEN= 5 * 1024 * 1024
    #CLIENT_ID = '224603931516-rff9gibtotfm6mljj278gdet57pa012t.apps.googleusercontent.com'
    #JWT_BLACKLIST_ENABLED=True
    #JWT_BLACKLIST_TOKEN_CHECKS=['access','refresh']

class Development(BaseConfig):
    DEBUG = True
    TESTING = True

class Production(BaseConfig):
    DEBUG = True
    TESTING = True
    DBHOST = 'localhost'
    DBUSER = 'root'
    DBPASS = 'root'
    DBNAME = 'wg'

