from flask import Flask
from multiprocessing import Process, Value, freeze_support
from multiprocessing.managers import BaseManager
import random
import time
from flask import url_for

from .State import State
from .routes import init_routes
from .dht_data import get_dht_data

def run_application():
    BaseManager.register('State', State)
    manager = BaseManager()
    manager.start()

    shared_state = manager.State()
    
    views = init_routes(shared_state)
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bardzo sekretny klucz'
    freeze_support()
    app.register_blueprint(views, url_prefix='/')
    
    read_from_dht_process = Process(target=get_dht_data, args=(shared_state,))
    
    read_from_dht_process.start()    
    app.run(debug=True, 
            host='10.0.1.207', 
            threaded=True, 
            use_reloader=False)
    # read_from_dht_process.join()
