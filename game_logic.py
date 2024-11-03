import flet as ft

def check_win(grid, all_tiles, symbol1):
    win_condition = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    
    win = False  # Initialize win flag

    for condition in win_condition:
        if grid[condition[0]] == grid[condition[1]] == grid[condition[2]] and grid[condition[0]] != "":
            symbol1.value = f'{grid[condition[0]]} has won.'
            symbol1.color = ft.colors.GREEN
            win = True
            symbol1.update()

            for t in all_tiles:
                t.on_click = None
                if 'X' in symbol1.value:
                    t.bgcolor = ft.colors.GREEN_200
                elif 'O' in symbol1.value:
                    t.bgcolor = ft.colors.BLUE_200
                t.update()
            break  # Stop checking further if a win is found

    # Check for draw condition if no win
    if not win and all(tile.content.value != "" for tile in all_tiles):
        symbol1.value = "It was a draw"
        symbol1.color = ft.colors.PURPLE_200
        symbol1.update()
        
        for t in all_tiles:
            t.bgcolor = ft.colors.PURPLE_200
            t.on_click = None
            t.update()



def symbol_place(grid, tile, symbol1, all_tiles):
    if 'X' in symbol1.value:
        symbol = 'O'
    elif 'O' in symbol1.value:
        symbol = 'X'

    if tile.data in '012345678':
        grid[int(tile.data)] = symbol

    check_win(grid, all_tiles, symbol1)

def p_turn(tile, symbol1, grid, all_tiles):
    if tile.content.value == "":
        if 'O' in symbol1.value:
            symbol1.value = "It is X's turn"
            symbol1.color = ft.colors.GREEN_200
            tile.bgcolor = ft.colors.BLUE_200
            tile.content.value = "O"

        else:
            symbol1.value = "It is O's turn"
            symbol1.color = ft.colors.BLUE_200
            tile.bgcolor = ft.colors.GREEN_200
            tile.content.value = "X"
        tile.content.color = ft.colors.BLACK    
        tile.content.size = 25
        tile.on_click = None
        tile.update()
        symbol_place(grid, tile, symbol1, all_tiles)
    
    symbol1.update()   

        


