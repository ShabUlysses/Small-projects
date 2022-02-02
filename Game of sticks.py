#!/usr/bin/env python
# coding: utf-8

# In[5]:


print("Let's play a game of sticks.")

sticks = int(input('How many sticks do you want to play with? '))
player_turn = 1

while sticks > 0:
    Player_move = int(input('How many sticks do you want to take, Player1? (1/2/3) '))
    if Player_move > 3 or Player_move <1:
        print('Incorrect input, pidor')
        continue
        
    sticks = sticks - Player_move
    print(f'{Player_move} sticks taken\n')
    print('Sticks remaining ', sticks)
    
    if sticks <= 0:
        print(f'No more sticks left. \nPlayer {player_turn} has lost')
    
    player_turn = 1 if player_turn == 2 else 2
    
    


# In[ ]:




