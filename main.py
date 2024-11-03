import flet as ft
from gui import gui_tiles


def main(page):
    global grid
    grid = ['1','2','3','4','5','6','7','8','9']
    page.title = 'TIC-TAC-TOE'
    symbol1 = ft.Text(value="It is X's turn", size=20, color=ft.colors.GREEN_200)
    
    gui_tiles(page, symbol1, grid)

ft.app(target=main)