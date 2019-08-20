from game.Models.GamesAction import add_seed_data
from game.Models.GamesModel import Games
from server import SQLSession

sess = SQLSession()
game = sess.query(Games).filter_by(plateform = 'PlayStation Vita').all()
res_l = []
for g in game:
    res_l.append(
        {
            'title': g.title, 
            'plateform': g.plateform, 
            'score': g.score, 
            'genre': g.genre, 
            'editors_choice': g.editor_choice
            }
        )

print(res_l)
sess.close()
#print(g)
#add_seed_data()