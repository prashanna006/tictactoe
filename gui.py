import flet as ft
from game_logic import p_turn  

def reset_game(grid, all_tiles, symbol1, page):
    # Reset the grid to its initial state
    for i in range(9):
        grid[i] = str(i + 1)

    # Reset each tile’s content and background color
    for tile in all_tiles:
        tile.content.value = ""
        tile.bgcolor = ft.colors.AMBER  # Original color
        tile.on_click = lambda e, t=tile: p_turn(t, symbol1, grid, all_tiles)
        tile.update()

    # Reset turn indicator
    symbol1.value = "It is X's turn"
    symbol1.update()
    page.update()


    
def gui_tiles(page, symbol1, grid):
    title = ft.Text(value="TIC - TAC - TOE", color=ft.colors.PINK_200, size=34)
    
    space = ft.Text(value="")
    
        
    tile_11 = ft.Container(
                    content=ft.Text(""),
                    data='0',
                    margin=5,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=100,
                    height=100,
                    border_radius=10,
                    ink=True,
                )
    
    tile_12 = ft.Container(
                    content=ft.Text(""),
                    data='1',
                    margin=5,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=100,
                    height=100,
                    border_radius=10,
                    ink=True,
            )
    
    tile_13 = ft.Container(
                    content=ft.Text(""),
                    data='2',
                    margin=5,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=100,
                    height=100,
                    border_radius=10,
                    ink=True,
            )
    
    tile_21 = ft.Container(
                    content=ft.Text(""),
                    data='3',
                    margin=5,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=100,
                    height=100,
                    border_radius=10,
                    ink=True,
            )
    
    tile_22 = ft.Container(
                    content=ft.Text(""),
                    data='4',
                    margin=5,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=100,
                    height=100,
                    border_radius=10,
                    ink=True,
            )
    
    tile_23 = ft.Container(
                    content=ft.Text(""),
                    data='5',
                    margin=5,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=100,
                    height=100,
                    border_radius=10,
                    ink=True,
            )
    
    tile_31 = ft.Container(
                    content=ft.Text(""),
                    data='6',
                    margin=5,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=100,
                    height=100,
                    border_radius=10,
                    ink=True,
            )
    
    tile_32 = ft.Container(
                    content=ft.Text(""),
                    data='7',
                    margin=5,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=100,
                    height=100,
                    border_radius=10,
                    ink=True,
            )
    
    tile_33 = ft.Container(
                    content=ft.Text(""),
                    data='8',
                    margin=5,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=100,
                    height=100,
                    border_radius=10,
                    ink=True,
            )
    
    all_tiles = [tile_11, tile_12, tile_13, tile_21, tile_22, tile_23, tile_31, tile_32, tile_33]
    refresh_button = ft.ElevatedButton(text="Refresh", on_click=lambda e: reset_game(grid, all_tiles, symbol1, page))
    
    
    tile_11.on_click= lambda e: p_turn(tile_11, symbol1, grid, all_tiles)
    tile_12.on_click= lambda e: p_turn(tile_12, symbol1, grid, all_tiles)
    tile_13.on_click= lambda e: p_turn(tile_13, symbol1, grid, all_tiles)
    tile_21.on_click= lambda e: p_turn(tile_21, symbol1, grid, all_tiles)
    tile_22.on_click= lambda e: p_turn(tile_22, symbol1, grid, all_tiles)
    tile_23.on_click= lambda e: p_turn(tile_23, symbol1, grid, all_tiles)
    tile_31.on_click= lambda e: p_turn(tile_31, symbol1, grid, all_tiles)
    tile_32.on_click= lambda e: p_turn(tile_32, symbol1, grid, all_tiles)
    tile_33.on_click= lambda e: p_turn(tile_33, symbol1, grid, all_tiles)

    
    row_1 = ft.Row(
        [
        tile_11,
        tile_12,
        tile_13,
    ], alignment=ft.MainAxisAlignment.CENTER
                   )
    
    row_2 = ft.Row(
        [
        tile_21,
        tile_22,
        tile_23,
    ], alignment=ft.MainAxisAlignment.CENTER
                   )
    
    row_3 = ft.Row(
        [
        tile_31,
        tile_32,
        tile_33,
    ], alignment=ft.MainAxisAlignment.CENTER
                   )
    page_add(page, row_1, row_2, row_3, title, symbol1, grid, all_tiles, refresh_button, space)


def page_add(page, row_1, row_2, row_3, title, symbol1, grid, all_tiles, refresh_button, space):
        
    page.add(
        ft.Row(
            [
            title
        ], alignment=ft.MainAxisAlignment.CENTER
            )
        )
    
    page.add(space)
        
    page.add(
        row_1,
        row_2,
        row_3,
    )
    
    
    page.add(
        ft.Row(
            [
                symbol1
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
    
    page.add(
        ft.Row(
            [refresh_button],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()

    return None