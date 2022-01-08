# conway game of life

import random, time, copy

width = 100
height = 40

nextCells = []

#create list for cells
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0,1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column)
    
#main program loop
while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    #print
    for y in range (height):
        for x in range (width): 
            print(currentCells[x][y], end= '')
        print()
        
    #calculate next step based on current step
    for x in range(width):
        for y in range(height):
            #get neighbouring coordinates where '%' ensure value between 0-1
            leftCoord = (x - 1) % width
            rightCoord = (x + 1) % width
            aboveCoord = (y - 1) % height
            belowCoord = (y + 1) % height
            
            #count number of living neighbours
            numNeibor = 0
            if  currentCells [leftCoord][aboveCoord] == '#':
                numNeibor += 1
            if currentCells [x][aboveCoord] == '#':
                numNeibor += 1
            if currentCells [aboveCoord][rightCoord] == '#':
                numNeibor += 1
            if currentCells [leftCoord][y] == '#':
                numNeibor += 1
            if currentCells [y][rightCoord] == '#':
                numNeibor += 1
            if currentCells [leftCoord][belowCoord] == '#':
                numNeibor += 1
            if currentCells [x][belowCoord] == '#':
                numNeibor += 1
            if currentCells [belowCoord][rightCoord] == '#':
                numNeibor += 1
                
            #set cell based on conway rules
            
            if currentCells[x][y] == '#' and (numNeibor == 2 or numNeibor ==3):
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeibor == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '
            time.sleep(1)   