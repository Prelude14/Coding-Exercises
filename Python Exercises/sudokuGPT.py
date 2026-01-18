import pprint #want this to print out the sudoku boards in more readable format

"""after completing the exercise I took my attempt to ChatGPT to see what could be done better, and this function is what I got. I had never heard of Python's "set" feature, which allowed them to 
   totally collapsed the logic down to way more readable code, so I'm looking into set to learn more and get better. Mine worked the exact same functionally, it just took 168 lines or so when this
   takes about 18 lol. I used about 7 for loops as well when this only needed two since it can check for every value at once. """
def validityChecker(board: list[list[str]]) -> bool:

    rows = [set() for _ in range(9)] #sets don't allow for duplicates to be added supposedly
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == ".":
                continue

            box_index = (i // 3) * 3 + (j // 3)

            if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                return False

            rows[i].add(val)
            cols[j].add(val)
            boxes[box_index].add(val)

    return True

def main():
   print("=" * 50)
   print(" Valid Sudoku EXERCISE")
   print("=" * 50)

   board1 = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

   print("\n Input board 1: ") #print board1 to console,
   pprint.pprint(board1)
   print("-" * 50)

   print("\n Output:") #print output of validity of board1
   print("-" * 50)
   print("\n", validityChecker(board1)) #send board1 to validity checker func to return if it is valid or not
   print("=" * 50)

   board2 = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["5",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

   print("\n Input board 2: ") #print board2 to console,
   pprint.pprint(board2)
   print("-" * 50)

   print("\n Output:") #print output of validity of board2
   print("-" * 50)
   print("\n", validityChecker(board2)) #send board1 to validity checker func to return if it is valid or not
   print("=" * 50)


if __name__ == "__main__":
   main()



   """


   3 4 5 no

   3 5 4 no

   4 3 5 works

   4 5 3 also works

   5 3 4 no

   5 4 3 also works
   

   """