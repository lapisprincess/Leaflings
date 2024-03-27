""" inventory screen to display player's items """

## IMPORTS ###
import pygame as pg

from gui.button import Button, back_to_game
from gui import Panel
from entity.player import Player


## CONSTANTS ###
FIELD_IMG = pg.image.load("data/leafy_field.jpg")


class Inventory(Panel):
    def __init__(
        self, 
        screen_dimensions: tuple[int, int], 
        fonts: pg.font.Font, 
        system, 
        player: Player
    ):
        Panel.__init__(self, (0, 0), screen_dimensions, fonts)

        # initialize static pieces
        self.blit(FIELD_IMG, (0, 0))

        self.rect_xpos = screen_dimensions[0] * 1/10
        self.rect_ypos = screen_dimensions[1] * 1/8
        self.rect_width = screen_dimensions[0] - self.rect_xpos*2
        self.rect_height = screen_dimensions[1] - self.rect_ypos*2
        rectangle = pg.Rect(
            self.rect_xpos, self.rect_ypos,
            self.rect_width, self.rect_height
        )
        pg.draw.rect(self, pg.Color(100, 150, 100), rectangle)

        render = self.fonts["h1"].render("Your stuff:", None, pg.Color(255, 255, 255))
        self.blit(render, (150, 100))

        render = self.fonts["li"].render("Return to game", None, pg.Color(0, 0, 0))
        exit_button = Button(
            pixel_coord= (self.rect_width-49, self.rect_ypos), 
            pixel_dimen= (150, 50), 
            color= pg.Color(200, 255, 200), 
            target= system, 
            function= back_to_game, 
            text= render
        )
        exit_button.draw(self)
        self.buttons.append(exit_button)


    def update_items(self, player):
        height = 150
        rectangle = pg.Rect(
            self.rect_xpos, self.rect_ypos+70,
            self.rect_width, self.rect_height
        )
        pg.draw.rect(self, pg.Color(100, 150, 100), rectangle)
        for item in player.inventory:

            render = self.fonts["li"].render('-', None, pg.Color(255, 255, 255))
            self.blit(render, (175, height))
            render = self.fonts["li"].render(item.info["name"], None, pg.Color(255, 255, 255))
            self.blit(render, (200, height))

            if len(self.buttons) - 1 > len(player.inventory) * 3:
                continue

            render = self.fonts["li"].render("View", None, pg.Color(255, 255, 255))
            view_button = Button(
                pixel_coord= (400, height-15),
                pixel_dimen= (80, 40), 
                color= pg.Color(100, 100, 100), 
                target= None,
                function= None,
                text= render
            )
            view_button.draw(self)
            self.buttons.append(view_button)

            render = self.fonts["li"].render("Use", None, pg.Color(255, 255, 255))
            use_button = Button(
                pixel_coord= (500, height-15),
                pixel_dimen= (80, 40), 
                color= pg.Color(100, 100, 100), 
                target= player,
                function= item.use,
                text= render
            )
            use_button.draw(self)
            self.buttons.append(use_button)

            render = self.fonts["li"].render("Drop", None, pg.Color(255, 255, 255))
            drop_button = Button(
                pixel_coord= (600, height-15),
                pixel_dimen= (80, 40), 
                color= pg.Color(100, 100, 100), 
                target= player,
                function= item.drop,
                text= render
            )
            drop_button.draw(self)
            self.buttons.append(drop_button)

            height += 50

        while len(self.buttons) - 1 > len(player.inventory) * 3:
            self.buttons.pop()