"""Simple Tic-Tac-Toe game"""
###### Python Packges ######

###### My Packges ######
from Engine.engine import PyEngine
from Engine.Libs.Designer.designer import Designer
from Engine.Libs.json_handler import read_json


game_setting = {"current": 1, "pads": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "win": 0}


if __name__ == "__main__":
    game = PyEngine()

    blue_print = read_json("UiData/blueprint.json")

    Designer.create_element("PyRect", blue_print.get("background"))
    Designer.create_element("PyRect", blue_print.get("player_text"))
    Designer.create_element("PyRect", blue_print.get("exit_bt"))
    Designer.create_element("PyRect", blue_print.get("reset_bt"))

    Designer.create_element("PyRect", blue_print.get("pad_1"))
    Designer.get_element("pad_1").rect.x -= 5
    Designer.get_element("pad_1").rect.y -= 5

    Designer.create_element("PyRect", blue_print.get("pad_2"))
    Designer.get_element("pad_2").rect.y -= 5

    Designer.create_element("PyRect", blue_print.get("pad_3"))
    Designer.get_element("pad_3").rect.x += 5
    Designer.get_element("pad_3").rect.y -= 5

    Designer.create_element("PyRect", blue_print.get("pad_4"))
    Designer.get_element("pad_4").rect.x -= 5

    Designer.create_element("PyRect", blue_print.get("pad_5"))

    Designer.create_element("PyRect", blue_print.get("pad_6"))
    Designer.get_element("pad_6").rect.x += 5

    Designer.create_element("PyRect", blue_print.get("pad_7"))
    Designer.get_element("pad_7").rect.x -= 5
    Designer.get_element("pad_7").rect.y += 5

    Designer.create_element("PyRect", blue_print.get("pad_8"))
    Designer.get_element("pad_8").rect.y += 5

    Designer.create_element("PyRect", blue_print.get("pad_9"))
    Designer.get_element("pad_9").rect.x += 5
    Designer.get_element("pad_9").rect.y += 5

    game.mainloop(Designer.draw_group)
