data11 =[[" ",9," ",8," "," "," ",5,7],
        [" "," ",6," "," ",1," ",2," "],
        [3," "," "," ",7," "," "," "," "],
        [5," "," ",9," ",6," ",3,8],
        [" ",3," "," ",1," "," "," "," "],
        [2," ",8," "," "," ",5,1," "],
        [6," "," "," ",9," "," "," ",3],
        [" ",1," "," "," "," "," ",9," "],
        [" "," ",7,6," ",5,8," "," "]]

data12 = [[" ",9," ",8," "," "," ",5,7],
        [" "," ",6," "," ",1," ",2," "],
        [3," "," "," ",7," "," "," "," "],
        [5," "," ",9," ",6," ",3,8],
        [" ",3," "," ",1," "," "," "," "],
        [2," ",8," "," "," ",5,1," "],
        [6," "," "," ",9," "," "," ",3],
        [" ",1," "," "," "," "," ",9," "],
        [" "," ",7,6," ",5,8," "," "]]

data21 = [[1," "," "," ",5," ",7," ",2],
        [" "," "," ",6," ",3," "," ",8],
        [" ",7,6," ",1," ",3," "," "],
        [" ",4," ",3," ",7," ",5," "],
        [8,1," "," ",6," ",4," ",7],
        [" ",9," "," "," ",5," "," "," "],
        [2,6," "," "," "," ",8," ",5],
        [9," "," ",8," ",1," "," "," "],
        [" "," ",3," ",9," "," ",2," "]]
data22 = [[1," "," "," ",5," ",7," ",2],
        [" "," "," ",6," ",3," "," ",8],
        [" ",7,6," ",1," ",3," "," "],
        [" ",4," ",3," ",7," ",5," "],
        [8,1," "," ",6," ",4," ",7],
        [" ",9," "," "," ",5," "," "," "],
        [2,6," "," "," "," ",8," ",5],
        [9," "," ",8," ",1," "," "," "],
        [" "," ",3," ",9," "," ",2," "]]
data31 = [[1,9,4,8,6,2,3,5,7],
        [8,7,6,3,5,1,9,2,4],
        [3,5,2,4,7,9,1,8,6],
        [5,4,1,9,2,6,7,3,8],
        [7,3,9,5," ",8,4,6,2],
        [2,6,8,7,4,3,5,1,9],
        [6,8,5,1,9,4,2,7,3],
        [4,1,3,2,8,7,6,9,5],
        [9,2,7,6,3,5,8,4,1]]
data32 = [[1,9,4,8,6,2,3,5,7],
        [8,7," ",3,5,1,9,2,4],
        [3,5,2,4,7,9,1,8,6],
        [5,4,1,9," ",6,7,3,8],
        [7,3,9,5," ",8,4,6,2],
        [2,6,8,7,4,3,5,1,9],
        [6,8,5,1,9,4,2,7,3],
        [4,1,3,2,8,7,6,9,5],
        [9,2,7,6,3,5,8,4,1]]
data41 = [[4," ",1,3,6," "," "," "," "],
        [6," "," ",2,5," "," ",9," "],
        [" ",5,3," ",1," "," ",4,2],
        [5," ",6,4," ",7," "," "," "],
        [" ",4," "," "," "," ",3,2,5],
        [1,8,2,9," "," "," ",6,4],
        [" "," "," "," "," ",1,9," ",8],
        [" "," "," ",6,7,3,2," "," "],
        [3,1,5," "," "," "," "," "," "]]
data42 = [[4," ",1,3,6," "," "," "," "],
        [6," "," ",2,5," "," ",9," "],
        [" ",5,3," ",1," "," ",4,2],
        [5," ",6,4," ",7," "," "," "],
        [" ",4," "," "," "," ",3,2,5],
        [1,8,2,9," "," "," ",6,4],
        [" "," "," "," "," ",1,9," ",8],
        [" "," "," ",6,7,3,2," "," "],
        [3,1,5," "," "," "," "," "," "]]

lt = [data11, data21, data41, data31]
et = [data12, data22, data42, data32]

m = int(input("Which sudoku table do you want?: (choose from 1 to 3)"))
m = m - 1
print("You can quit during the game at any point if you press 'Q' at any question.")
print("You can delete during the game at any point if you press 'D' at any question.")
print("You can check the finished sudoku with 'F'.")

#this one
def Print_Game():
    print('{:-^27s}'.format("Sudoku game"))

    print("    1", "2", "3", "  4", "5", "6", "  7", "8", "9")
    print("  -------------------------")
    for i in range(0, 3):
        print('{} | {} {} {} | {} {} {} | {} {} {} |'.format(i+1, lt[m][i][0],lt[m][i][1],lt[m][i][2],lt[m][i][3], lt[m][i][4], lt[m][i][5], lt[m][i][6], lt[m][i][7], lt[m][i][8]))
    print("  |-------+-------+-------|")

    for i in range(3, 6):
        print('{} | {} {} {} | {} {} {} | {} {} {} |'.format(i+1, lt[m][i][0],lt[m][i][1],lt[m][i][2],lt[m][i][3], lt[m][i][4], lt[m][i][5], lt[m][i][6], lt[m][i][7], lt[m][i][8]))
    print("  |-------+-------+-------|")

    for i in range(6, 9):
        print('{} | {} {} {} | {} {} {} | {} {} {} |'.format(i+1, lt[m][i][0],lt[m][i][1],lt[m][i][2],lt[m][i][3], lt[m][i][4], lt[m][i][5], lt[m][i][6], lt[m][i][7], lt[m][i][8]))
    print("  -------------------------")

def linearCheck():
    endnum = 0
    for i in range(0, 9):
        avg = 0
        for j in range(0, 9):
            avg = (avg + (lt[m][i][j]))
        
        endnum = (avg / 9)
        if endnum != 5:
            print("there is a wrong number in the", i + 1,". line")
            

def horizontalCheck():
    for i in range(0, 9):
        avg = 0
        for j in range(0, 9):
            avg = avg + (lt[m][j][i])
        endnum = (avg / 9)
        if endnum != 5:
            print("There is a wrong number in the", i+1,". coloumn.")
            wrong1 = input("If you want to delete the wrong number press 'D':")  
            if wrong1 =='D' or wrong1 =='d':
                    DeleteChoosen()
    
    print("Everything seems ok!")
    raise SystemExit     

def CheckInput(x, y):     
    if et[m][x-1][y-1] == " ":
        return True
    elif et[m][x-1][y-1] == 1 or 2 or 3 or 4 or 5 or 7 or 8 or 9:
        return False

print(Print_Game()) 


def DeleteChoosen():
    c = int(input("Write the line you want to delete: "))
    v = int(input("Write the coloumn you want to change: "))
    if CheckInput(c, v) == True:                
        lt[m][c-1][v-1]= str(lt[m][c-1][v-1]) 
        lt[m][c-1][v-1]= " " 
        print(Print_Game())
        Main()
    else:
        print("Error")
       


def Main():
    n = []
    while True:
        a = input("Give a number [rows] [columns] [number to write], e.g: (3 5 7) ")
        n = a.split()
        if n[0] == "Q" or n[0] == "q":
            break
        elif n[0] == "H" or n[0] == "h" :
            print("Welcome to our game!\nThis game follows the classic soduku rules.\nMade by.Andrea & Bence.")
        elif n[0] == "D" or n[0] == "d":
            DeleteChoosen()
            continue
        elif n[0] == "F" or n[0] == "f":
            linearCheck()
            horizontalCheck()   
        else:
            n1 = int(n[0])
            n2 = int(n[1])
            n3 = int(n[2])
            if CheckInput(n1, n2) == True:                
                lt[m][n1 - 1][n2 - 1] = n3
                print(Print_Game()) 
            else:
                print("Invalid Number")



Main()

