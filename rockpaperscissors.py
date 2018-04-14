# 2 players
# ask each for input
# compare
# print message congratulating winnner
# ask players if they want to play again

# TO DO: circular array in HB


############### VERSION 1 ################


def get_input(player_string):
    """Get valid choices for rock, paper, scissors game. Returns two strings."""

    print "\n{}: choose (R)ock, (P)aper, or (S)cissors...".format(player_string)

    player_choice = raw_input("Enter R, P, or S >  ").upper()
    if not (player_choice == "R" or "P" or "S"):  # validate with assert instead?
        print "Not a valid choice."
        get_input(player_string)

    return player_choice


def compare_inputs(player_1, player_2):

    message = ""

    # First check they are the same
    if player_1 == player_2:
        message = "You tied!"

    # First player chooses rock
    elif player_1 == "R":
        if player_2 == "P":
            message = "Player 2 wins!"
        else:  # player_2 == "S":
            message = "Player 1 wins!"

    elif player_1 == "P":
        if player_2 == "R":
            message = "Player 1 wins!"
        else:  # player_2 == "S":
            message = "Player 2 wins!"

    else:  # player_1 == "S":
        if player_2 == "R":
            message = "Player 2 wins!"
        else:  # player_2 == "P":
            message = "Player 1 wins!"

    print message


def will_play_again():

    replay = raw_input("Play again? Type Y to play again, or anything else to quit. >  ").upper()
    if replay == "Y":
        play_rps_game()
    else:
        print "Thanks for playing, friends!"


def play_rps_game():
    """Gets inputs, evaluates player choices, declares winner,
    determines continuation of game."""

    player_1 = get_input("Player 1")
    player_2 = get_input("Player 2")

    compare_inputs(player_1, player_2)

    will_play_again()


if __name__ == "__main__":

    play_rps_game()
    import doctest
    # if doctest.testmod.failed == 0:
    #     print "Good game!"
