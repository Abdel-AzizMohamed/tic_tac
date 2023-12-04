"""Define x/o game functions"""
###### Python Packges ######
import sys
import pygame

# pylint: disable=E1101
###### My Packges ######
from main import game_setting
from Engine.Libs.Designer.designer import Designer


def switch_player(ele, index):
    """Switch current player"""
    row = index[0]
    col = index[1]
    if game_setting["pads"][row][col] != 0 or game_setting["win"] != 0:
        return

    add_x_o(ele, index)

    if game_setting.get("current") == 1:
        game_setting["current"] = 2
        Designer.get_element("player_text").update_text(text="Player 2 Turn")
    else:
        game_setting["current"] = 1
        Designer.get_element("player_text").update_text(text="Player 1 Turn")


def add_x_o(ele, index):
    """Add x/o to pad"""
    row = index[0]
    col = index[1]
    if game_setting["pads"][row][col] != 0 or game_setting["win"] != 0:
        return

    if game_setting.get("current") == 1:
        ele.update_text(text="X")
        game_setting["pads"][row][col] = 1
    else:
        ele.update_text(text="O")
        game_setting["pads"][row][col] = 2


def check_win(_):
    """Check if a player Won the game"""
    pads = game_setting.get("pads")
    for i in range(3):
        if pads[i][0] == 1 and pads[i][1] == 1 and pads[i][2] == 1:
            Designer.get_element("player_text").update_text(text="Player 1 Won")
            game_setting["win"] = 1
        elif pads[i][0] == 2 and pads[i][1] == 2 and pads[i][2] == 2:
            Designer.get_element("player_text").update_text(text="Player 2 Won")
            game_setting["win"] = 1

    for i in range(3):
        if pads[0][i] == 1 and pads[1][i] == 1 and pads[2][i] == 1:
            Designer.get_element("player_text").update_text(text="Player 1 Won")
            game_setting["win"] = 1
        if pads[0][i] == 2 and pads[1][i] == 2 and pads[2][i] == 2:
            Designer.get_element("player_text").update_text(text="Player 2 Won")
            game_setting["win"] = 1

    if pads[0][0] == 1 and pads[1][1] == 1 and pads[2][2] == 1:
        Designer.get_element("player_text").update_text(text="Player 1 Won")
        game_setting["win"] = 1
    if pads[0][2] == 1 and pads[1][1] == 1 and pads[2][0] == 1:
        Designer.get_element("player_text").update_text(text="Player 1 Won")
        game_setting["win"] = 1

    if pads[0][0] == 2 and pads[1][1] == 2 and pads[2][2] == 2:
        Designer.get_element("player_text").update_text(text="Player 2 Won")
        game_setting["win"] = 1
    if pads[0][2] == 2 and pads[1][1] == 2 and pads[2][0] == 2:
        Designer.get_element("player_text").update_text(text="Player 2 Won")
        game_setting["win"] = 1


def exit_game(_):
    """Exit game"""
    pygame.quit()
    sys.exit()


def reset_game(_):
    """Reset game"""
    global game_setting

    game_setting = {"current": 1, "pads": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "win": 0}
    Designer.get_element("player_text").update_text(text="Player 1 Turn")

    for i in range(1, 10):
        Designer.get_element(f"pad_{i}").update_text(text="")
