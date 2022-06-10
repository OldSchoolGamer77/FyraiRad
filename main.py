# coding=utf-8

import pygame
import os
import sys
import math
from gameInfo import GameInfo
import json

game_info = GameInfo()

def start():
    game_info.netThread.net.send("Player", "What is?")
    game_info.player = int(game_info.netThread.net.receive())


def get_board():
    game_info.netThread.net.send("Get", "Board") 
    board_array = game_info.netThread.net.receive()
    print(board_array) 
    board_array = json.loads(board_array)
    return board_array


def player_move(col):
    game_info.netThread.net.send(col, "Move")


def print_board(board_array):
    print(board_array)


def draw_ui(board_array):
    for c in range(game_info.COLS):
        for r in range(game_info.ROWS):
            pygame.draw.rect(game_info.screen, game_info.BLUE, 
                             (c*game_info.SQUARE_SIZE,
                              r*game_info.SQUARE_SIZE+
                              game_info.SQUARE_SIZE, 
                              game_info.SQUARE_SIZE, 
                              game_info.SQUARE_SIZE)
            )
            
            pygame.draw.circle(game_info.screen, game_info.BLACK, 
                               (int(c*game_info.SQUARE_SIZE+
                                    game_info.SQUARE_SIZE/2), 
                                int(r*game_info.SQUARE_SIZE+
                                    game_info.SQUARE_SIZE+
                                    game_info.SQUARE_SIZE/2)), 
                                    game_info.CHIP_SIZE
            )
    
    for c in range(game_info.COLS):
        for r in range(game_info.ROWS):
            print (board_array[r])
            if board_array[r][c] == 1:
                pygame.draw.circle(game_info.screen, game_info.RED, 
                                   (int(c*game_info.SQUARE_SIZE+
                                        game_info.SQUARE_SIZE/2), 
                                        game_info.height-
                                    int(r*game_info.SQUARE_SIZE+
                                        game_info.SQUARE_SIZE/2)), 
                                        game_info.CHIP_SIZE
            )
        
    for c in range(game_info.COLS):
        for r in range(game_info.ROWS):
            if board_array[r][c] == 2:
                pygame.draw.circle(game_info.screen, game_info.YELLOW, 
                                   (int(c*game_info.SQUARE_SIZE+
                                        game_info.SQUARE_SIZE/2),
                                        game_info.height-
                                    int(r*game_info.SQUARE_SIZE+
                                        game_info.SQUARE_SIZE/2)), 
                                        game_info.CHIP_SIZE
            )
    
    pygame.display.update()

board_array = get_board()
print_board(board_array)
start()

pygame.init()


draw_ui(board_array)
pygame.display.update()

while game_info.no_winner:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            game_info.netThread.net.disconnect()
            game_info.no_winner = False

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(game_info.screen, game_info.BLACK, 
                             (0,0, 
                              game_info.width, 
                              game_info.SQUARE_SIZE)
            )
            
            game_info.mousex = event.pos[0]
            
            if game_info.player == 1:
                pygame.draw.circle(game_info.screen, game_info.RED, 
                                   (game_info.mousex, 
                                    int(game_info.SQUARE_SIZE/2)), 
                                   game_info.CHIP_SIZE
                )

                pygame.display.update()
            
            elif game_info.player == 2:
                pygame.draw.circle(game_info.screen, game_info.YELLOW, 
                                   (game_info.mousex, 
                                    int(game_info.SQUARE_SIZE/2)), 
                                   game_info.CHIP_SIZE
                )
                
                pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(game_info.screen, game_info.BLACK, 
                             (0, 0, 
                              game_info.width, 
                              game_info.SQUARE_SIZE)
            )
            print("befor if")
            if game_info.player == 1:
                print("Player 1 before move")
                game_info.mousex = event.pos[0]
                col = int(math.floor(game_info.mousex/game_info.SQUARE_SIZE))
                player_move(col)
                print("Player 1 after move")
                
                is_valid_move = game_info.netThread.net.receive()
                print("after is valid move before if")
                if is_valid_move == 0:
                    print("is valid move before cont")
                    continue
                

                else:
                    board_array = is_valid_move
                    board_array = json.loads(board_array)
                    print("else is valid move before win")
                    win = game_info.netThread.net.receive()
                    print("else if win Player 1")
                    #if win != 0:
                        #msg = game_info.win_msg.render("Player 1 wins!", 1, game_info.RED)
                        #game_info.screen.blit(msg, (30,6))
                        #no_winner = False
            

                            
            #elif game_info.player == 2:
            else:
                print("Player 2 before move")
                game_info.mousex = event.pos[0]
                col = int(math.floor(game_info.mousex/game_info.SQUARE_SIZE))
                player_move(col)
                print("Player 2 after move")
                 
                
                is_valid_move = game_info.netThread.net.receive()
               
                if is_valid_move == 0:
                    print("Is valid move before cont")
                    continue
                
                else:
                    board_array = is_valid_move
                    board_array = json.loads(board_array)
                    win = game_info.netThread.net.receive()
                    print("else if win Player 2")
                    #if win != 0:
                        #msg = game_info.win_msg.render("Player 2 wins!", 1, game_info.YELLOW)
                        #game_info.screen.blit(msg, (30,6))
                        #no_winner = False
                


            print_board(board_array)
            draw_ui(board_array)

            if game_info.no_winner == False:
                pygame.time.wait(3000)

    
    game_info.clock.tick(game_info.FRAMERATE) 



