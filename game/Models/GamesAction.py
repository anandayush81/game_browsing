from game.Models.GamesModel import Games
from flask import request, Blueprint, jsonify

def add_game(data):
    from server import SQLSession
    session = SQLSession()
    game = session.query(Games).filter_by(title = data['title']).first()
    if not game:
        new_game = Games(
            data['title'],
            data['plateform'],
            data['score'],
            data['genre'],
            data['editors_choice']
        )
        try:
            session.add(new_game)
            session.commit()
            print("OK")
        except:
            res = {
                'status': 'Fail',
                'message': 'error in db'
            }
            print("NOT db")
            #return jsonify(res)
        finally:
            res = {
                'status': 'OK',
                'message': 'successfully added'
            }
            #return jsonify(res)
    else:
        res = {
                'status': 'Fail',
                'message': 'already_exist'
            }
        #return jsonify(res)
    

def add_seed_data():
    import pandas as pd
    import os
    seed_data = pd.read_csv(os.getcwd()+"/game/Models/seed.csv")
    log = []
    for i, r in seed_data.iterrows():
        data = {}
        data['title'] = r['title']
        data['plateform'] = r['platform']
        data['score'] = r['score']
        data['genre'] = r['genre']
        if(r['editors_choice']=='Y'):
            data['editors_choice'] = True
        else:
            data['editors_choice'] = True
        log.append(add_game(data))
    

if __name__ == "__main__":
    add_seed_data()    
    