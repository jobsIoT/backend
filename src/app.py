from src.db import recreate_database, create_app
from src.db import app, api
from src.ressources.inscription import Inscription
from src.ressources.connexion import Connexion
from src.ressources.user_manage import User_manage
from src.ressources.modify_user import Modify_user
from src.ressources.send_pulls import Send_pulls
from src.ressources.home import Home

api.add_resource(Inscription, '/inscription')
api.add_resource(Connexion, '/connexion')
api.add_resource(User_manage, '/user')
api.add_resource(Modify_user, '/modify_user')
api.add_resource(Send_pulls, '/send_pulls')
api.add_resource(Home, '/')

if __name__ == '__main__':
    create_app()
    app.run()