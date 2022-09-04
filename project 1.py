# 1 minute math game
# 1ST project from the challenge. Tried doing it without eval() and 

import time
import random as r

fim = time.time() + 60
total = 0
strike = 0
operations = ['+', '-', '*', '/']

def game(op):
    equation = ""
    a = r.randint(1,100)
    
    sign = r.choice(op)
    
    if sign == '/':
        multiples = []
        for i in range (1, a+1):
            if a % i == 0:
                multiples.append(i)
        b = r.choice(multiples)

        r_ans = a/b
        
    else:
        b = r.randint(1,100)

        if sign == '+':
            r_ans = a + b
        elif sign == '-':
            r_ans = a - b
        else:
            r_ans =  int(a*b)

        
    equation = equation + str(a) + str(sign) + str(b)

    
    ans = input ( equation + ' = ' )

    if type(ans) != int :
        print('Only number please.')
        return False
    

    if ans == r_ans:
        print('Correct! :)' )
        return True
    else:
        print('Wrong! The right answer was ', r_ans)
        return False

if __name__ == '__main__':
    
    while time.time() < fim:

        if game(operations) == True:
            strike = strike + 1

        total = total + 1
        

    score = (strike / total)*100
    print( 'End of game! You got %.2f of the questions right.' % score)
