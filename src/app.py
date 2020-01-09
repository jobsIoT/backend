from src.db import recreate_database, create_app
from src.db import app, api
from src.ressources.inscription import Inscription
from src.ressources.connexion import Connexion
from src.ressources.user_manage import User_manage
from src.ressources.modify_user import Modify_user
from src.ressources.send_pulls import Send_pulls
from src.ressources.get_pulls import getPulls
from src.ressources.get_journeys import getJourneys
from src.ressources.home import Home
from src.ressources.get_users import getUsers
from src.ressources.del_user import delUser

api.add_resource(Inscription, '/inscription')
api.add_resource(Connexion, '/connexion')
api.add_resource(User_manage, '/user')
api.add_resource(Modify_user, '/modify_user')
api.add_resource(Send_pulls, '/send_pulls')
api.add_resource(getPulls, '/get_pulls')
api.add_resource(getUsers, '/get_users')
api.add_resource(getJourneys, '/get_journeys')
api.add_resource(delUser, '/del_user')
api.add_resource(Home, '/')

if __name__ == '__main__':
    create_app()
    app.run()