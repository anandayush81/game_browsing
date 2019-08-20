import sys
import os
sys.path.append(os.getcwd())
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from game.config import DevelopmentConfig, config_by_name
from game import create_db_engine, create_db_sessionFactory
from game.Models import createTables
from game.API import gameBP, searchBP



config_name = 'dev'


engine = create_db_engine(DevelopmentConfig)
createTables(engine)
SessionFactory = create_db_sessionFactory(engine)
SQLSession = create_db_sessionFactory(engine)


app = Flask(__name__)
app.config.from_object(config_by_name[config_name])

@app.route('/')
def get():
    return "Hello"


app.register_blueprint(gameBP, url_prefix='/games')
app.register_blueprint(searchBP, url_prefix='/search')



if __name__ == "__main__":
    app.run(debug=True)