
# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result

def print_result(human_play_first):
    human_score, draw_score, computer_score = 0, 0, 0
    while True:
        result = play_once(human_play_first)
        if result == -1  :
            print("I win")
            human_score += 1
        elif result == 0:
            print("Game drawn")
            draw_score += 1
        elif result == 1:
            print("You win")
            computer_score += 1
        else:
            print("Invalid result")
            break

        print("Human {} , Draw {} , Computer {}".format(human_score, draw_score, computer_score))
        print("Percent human win {}%".format(human_score*100/(human_score+draw_score+computer_score)))
        i = input("Do you want to play again Y/N ? ")
        if i != "Y":
            print("Good bye")
            break
for i in range(100) :
    print_result(1)