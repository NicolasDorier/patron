from config import Config
from flask import Flask
from flask_blogging_protected import ProtectedBloggingEngine, ProtectedSQLAStorage
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_principal import Permission, RoleNeed
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(Config)

# extensions
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
protected_sql_storage = ProtectedSQLAStorage(db=db)
db.create_all()
protected_blog_engine = ProtectedBloggingEngine(app, protected_sql_storage)
login = LoginManager(app)
mail = Mail(app)

# permissions - flask_principal objects created by BloggingEngine
principals = protected_blog_engine.principal
admin_permission = Permission(RoleNeed('admin'))

# blueprints
from app.api import bp as api_bp
from app.auth import bp as auth_bp
from app.admin import bp as admin_bp
from app.main import bp as main_bp
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(main_bp)

from app import models
