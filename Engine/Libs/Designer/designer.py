"""Define the designer packge start point"""
###### Python Packges ######
import pygame

###### My Packges ######
from Engine.window import win_obj
from Engine.Libs.error_handler import data_check
from Engine.Libs.eventer import Eventer
from Engine.Libs.Designer.py_elements import PyRect


class Designer:
    """
    Define the main grahpic helper

    Attributes:
            elements_classes: Contains all the elements classes
            game_elements: dict of all game elements
    """

    elements_classes = {"PyRect": PyRect}
    game_elements = {}

    @staticmethod
    def create_element(ele_class, ele_attributes):
        """
        creates a new element

        Arguments:
            ele_class: element class name
            ele_attributes: element attributes (text, color, ...)
        """
        data_check(ele_attributes, dict)

        ele_group = ele_attributes.get("group")
        ele_name = ele_attributes.get("name")

        data_check(ele_name, str)
        data_check(ele_group, str)

        element = Designer.elements_classes[ele_class](ele_attributes)

        Eventer.add_object_event(element, ele_attributes.get("events"))

        if not Designer.game_elements.get(ele_group):
            Designer.game_elements[ele_group] = {}

        Designer.game_elements.get(ele_group)[ele_name] = element

    def read_ui(self, file_path):
        """read given ui file"""

    @staticmethod
    def get_element(name):
        """
        gets element by its name

        Arguments:
            name: name to search for
        """
        data_check(name, str)

        elements = [
            (key, item)
            for group in Designer.game_elements.values()
            for (key, item) in group.items()
        ]
        for key, item in elements:
            if key == name:
                return item
        return None

    @staticmethod
    def draw_group():
        """draw elements on screen"""
        elements = [
            item for group in Designer.game_elements.values() for item in group.values()
        ]
        for item in elements:
            if item.type == "rect":
                pygame.draw.rect(win_obj.screen, item.rect_color, item.rect)

            if getattr(item, "font_render"):
                x_pos = item.rect.x + item.align_x
                y_pos = item.rect.y + item.align_y
                win_obj.screen.blit(item.font_render, (x_pos, y_pos))
