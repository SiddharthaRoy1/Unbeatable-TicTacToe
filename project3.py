import math
from random import choice
human=-10
machine=+10
mat=['0']*10
mat2=[' ']*10
def printBoard(matrix):
    print('                             ',matrix[1],'|',matrix[2],'|',matrix[3])
    print('                             ','--+---+--')
    print('                             ',matrix[4],'|',matrix[5],'|',matrix[6])
    print('                             ','--+---+--')
    print('                             ',matrix[7],'|',matrix[8],'|',matrix[9])


def winningstate(matrix,player):
    win_state=[
        [matrix[1],matrix[2],matrix[3]],
        [matrix[4],matrix[5],matrix[6]],
        [matrix[7],matrix[8],matrix[9]],
        [matrix[1],matrix[4],matrix[7]],
        [matrix[2],matrix[5],matrix[8]],
        [matrix[3],matrix[6],matrix[9]],
        [matrix[1],matrix[5],matrix[9]],
        [matrix[3],matrix[5],matrix[7]],
    ]
    if [player,player,player]in win_state:
        return True
    else:
        return(False)


def gameover(matrix):
    return winningstate(matrix, human) or winningstate(matrix, machine)


def evaluate(matrix,dept):
    if winningstate(matrix, machine):
        score = 10+dept
    elif winningstate(matrix, human):
        score = -10+dept
    else:
        score = 0

    return score


def emptychecker(matrix):
    empty=[]
    for i in range(1,10):
        if matrix[i]=='0':
            empty.append(i)
    return empty


def minimax(matrix,depth,player):
    #print('er',emptychecker(matrix))
    if player==machine:
        best=[-1,-100000000]
    else:
        best=[-1,100000000]
    if depth==0 or gameover(matrix):
        score=evaluate(matrix,depth)
        return [-1,score]
    for i in emptychecker(matrix):
        
        matrix[i]=player
        score=minimax(matrix,depth-1,-player)
        #print(score)
        matrix[i]="0"
        score[0]=i
        #print('drg',i,score)
        if player==machine:
            if score[1]>best[1]:
                best=score
        else:
            if score[1]<best[1]:
                 best=score
    return best


def machineturn(matrix,matrix2,c_choice):
    depth=len(emptychecker(matrix))
    if depth==0 or gameover(matrix):
        return
    print("computer turn")
    if depth==9:
        r=choice([1,2,3,4,5,6,7,8,9])
    else:
        move=minimax(matrix,depth,machine)
        r=move[0]
    
    matrix[r]=machine
    matrix2[r]=c_choice
    printBoard(matrix2)


def humanturn(matrix,matrix2,h_choice):
    depth=len(emptychecker(matrix))
    if depth==0 or gameover(matrix):
        return
    print("human turn")
    humanvalue=int(input('1-9:'))
    matrix[humanvalue]=human
    matrix2[humanvalue]=h_choice
    printBoard(matrix2)


def main():
    h_choice=input("Choose X or O:").upper()
    if h_choice=="X":
        c_choice="O"
    else:
        c_choice="X"
    first=input("First to start(Y/N):").upper()
    for i in range(1,10):
        if not gameover(mat):
            if first=='N':
                machineturn(mat,mat2,c_choice)
                first=''
            humanturn(mat,mat2,h_choice)
            machineturn(mat,mat2,c_choice)
        if winningstate(mat,human):
            print('You win!!!')
            break
        elif winningstate(mat,machine):
            print('You lose!!!')
            break
    else:
        print("Draw!!!")


if __name__=='__main__':
    main()
    
    
    



                
    

            
