# TicTacNo

A quick joke project.

The `main.py` file includes every possible [Tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe) (noughts and crosses) position.

Over 102 MB and 2239393 lines of pure code greatness. 

<br/>

Moves are an index of the square, with the top-left square being `0`.

| **0** | **1** | **2** |
|:-----:|:-----:|:-----:|
| **3** | **4** | **5** |
| **6** | **7** | **8** |

<br/>

**Make sure you've got enough free RAM before running the file.**

---

### Output

```
This is the current board state:
X O X
O - -
X - -

Choose your move: 8


This is the current board state:
X O X
O - -
X - O

Choose your move: 4


This is the current board state:
X O X
O X -
X - O
Game over.
```

### Code sample

```python
if m == 6:      
 print('\n\nThis is the current board state:\nX O X\nO - X\nO - -\n')       
 m = int(input('Choose your move: '))       
 if m == 4:       
  print('\n\nThis is the current board state:\nX O X\nO X X\nO - -\n')        
  m = int(input('Choose your move: '))        
  if m == 7:        
   print('\n\nThis is the current board state:\nX O X\nO X X\nO O -\n')         
   m = int(input('Choose your move: '))         
   if m == 8:         
    print('\n\nThis is the current board state:\nX O X\nO X X\nO O X\nGame over.')          
    exit()          
   print('Invalid move.')         
   exit()         
  if m == 8:        
   print('\n\nThis is the current board state:\nX O X\nO X X\nO - O\n')         
   m = int(input('Choose your move: '))         
   if m == 7:         
    print('\n\nThis is the current board state:\nX O X\nO X X\nO X O\nGame over.')          
    exit()          
   print('Invalid move.')         
   exit()         
  print('Invalid move.')        
  exit()        
 if m == 7:       
  print('\n\nThis is the current board state:\nX O X\nO - X\nO X -\n')        
  m = int(input('Choose your move: '))        
  if m == 4:        
   print('\n\nThis is the current board state:\nX O X\nO O X\nO X -\n')         
   m = int(input('Choose your move: '))         
   if m == 8:         
    print('\n\nThis is the current board state:\nX O X\nO O X\nO X X\nGame over.')          
    exit()          
   print('Invalid move.')         
   exit()        
```


















