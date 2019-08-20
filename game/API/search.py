from flask import request, Blueprint, jsonify
from game.Models.GamesModel import Games

searchBP = Blueprint('seachApi', __name__)

def games_by_platform(data):
    from server import SQLSession
    session = SQLSession()
    game = session.query(Games).filter_by(title = data['title']).all()
    l = []
    if not game:
        return l
    else:
        l = []
        for g in game:
            l.append({'title': g.title, 'plateform': g.plateform, 'score': g.score, 'genre': g.genre, 'editors_choice': g.editor_choice})
    return l

@searchBP.route('/', methods = ['POST'])
def get_game_by_plateform():
    data = request.json
    da = games_by_platform(data)
    if(len(da) == 0):
        res = {
            'status': 'Not Ok',
            'message': 'No such title'
        }
    else:
        res = {
            'status': 'OK',
            'data': da
        }
    return jsonify(res), 200