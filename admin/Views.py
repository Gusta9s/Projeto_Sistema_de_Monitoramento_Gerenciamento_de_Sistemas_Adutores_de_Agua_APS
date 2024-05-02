from flask_admin import AdminIndexView, expose
from flask import redirect
from config import app_config, app_active
from model import *

config = app_config[app_active]

class HomeView(AdminIndexView):

    @expose('/')
    def index(self):
        return self.render('home.html')
    
    