import name
import game
import result


player1 = name.enter_name(1)
player2 = name.enter_name(2)

score1 = game.game(player1)
score2 = game.game(player2)

result.result(player1, player2, score1,score2)
