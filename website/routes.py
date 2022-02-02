from flask import Blueprint, jsonify, render_template
import random


def init_routes(shared_state):
    views = Blueprint('views', __name__)

    @views.route('/')
    def home():
        return render_template("base.html", test = shared_state.get_data())
    

    @views.route('/data', methods=['GET'])
    def data():
        val_temp = round(random.uniform(20,30),1)
        val_hum = round(random.uniform(40,60),1)
        # state.add_data(round(random.uniform(20,30),1), round(random.uniform(40,60),1))

        print({'data': shared_state.get_data()})
        return jsonify(shared_state.get_data())


    @views.route('/debug', methods=['GET'])
    def debug():
        shared_state.add_data(round(random.uniform(20,30),1), round(random.uniform(40,60),1))
        print(shared_state.get_data())
        return {'val':shared_state.get_data()}
    return views
