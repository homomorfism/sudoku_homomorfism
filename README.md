# sudoku_homomorfism

This repo contains programming assigment of Sudoku solver Task

How to run program:

```python
python main.py
```

Example of usage:

User (example from test, partially generated field):

```bash
How many point to generate? default - 0. $ Game is creating!
Now we are ready to play! Plotting field...
[[0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0]]
[[5 8 1 6 7 2 4 3 9]
 [7 9 2 8 4 3 6 5 1]
 [3 6 4 5 9 1 7 8 2]
 [4 3 8 9 5 7 2 1 6]
 [2 5 6 1 8 4 9 7 3]
 [1 7 9 3 2 6 8 4 5]
 [8 4 5 2 1 9 3 6 7]
 [9 1 3 7 6 8 5 2 4]
 [6 2 7 4 3 5 1 9 0]]
Wants to save game: yes - 1, no - 0, default: 0. $ 
Enter row, column and value to put number(in format: $1 5 7). $ 9 9 8
[[5 8 1 6 7 2 4 3 9]
 [7 9 2 8 4 3 6 5 1]
 [3 6 4 5 9 1 7 8 2]
 [4 3 8 9 5 7 2 1 6]
 [2 5 6 1 8 4 9 7 3]
 [1 7 9 3 2 6 8 4 5]
 [8 4 5 2 1 9 3 6 7]
 [9 1 3 7 6 8 5 2 4]
 [6 2 7 4 3 5 1 9 8]]
```

Computer:

```bash
/home/shamil/PycharmProjects/ML_Foundations_course/venv/bin/python /home/shamil/PycharmProjects/sudoku_homomorfism/main.py
Who plays: 0 - human, 1 - computer, default: human. $ 1
Ok, plays computer
How many point to generate? default - 0. $ 5
Game is creating!
Now we are ready to play! Plotting field...
[[0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0]
 [0 5 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0]
 [0 0 8 0 9 0 0 0 0]
 [0 0 0 0 0 0 0 0 0]
 [0 8 0 0 0 0 6 0 0]
 [0 0 0 0 0 0 0 0 0]]
[[1 2 3 4 5 6 7 8 9]
 [4 6 5 7 8 9 1 2 3]
 [8 7 9 1 2 3 4 5 6]
 [2 5 1 3 4 7 9 6 8]
 [3 9 6 2 1 8 5 4 7]
 [7 4 8 6 9 5 2 3 1]
 [5 1 7 8 6 2 3 9 4]
 [9 8 4 5 3 1 6 7 2]
 [6 3 2 9 7 4 8 1 5]]
The solution was found!
[[1 2 3 4 5 6 7 8 9]
 [4 6 5 7 8 9 1 2 3]
 [8 7 9 1 2 3 4 5 6]
 [2 5 1 3 4 7 9 6 8]
 [3 9 6 2 1 8 5 4 7]
 [7 4 8 6 9 5 2 3 1]
 [5 1 7 8 6 2 3 9 4]
 [9 8 4 5 3 1 6 7 2]
 [6 3 2 9 7 4 8 1 5]]

Process finished with exit code 0
```

