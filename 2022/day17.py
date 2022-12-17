with open("in.txt") as _:
    f = _.read().split("\n")
    IN = [x for x in f]

IN = IN[0]

rocks = [[(0,1),(1,1),(2,1),(3,1)], 
[(1,1),(0,2),(1,2),(2,2),(1,3)],
[(2,2),(2,3), (0,1),(1,1),(2,1)],
[(0,1),(0,2),(0,3),(0,4)],
[(0,1),(1,1),(0,2),(1,2)]
]

# IN = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

dir_i = 0
rock_i = 0
top = 0
dropping = None

rockpos = {(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)}

# print = open("out.txt", 'w').write

def printboard():
    for y in range(10000, 0, -1):
        for x in range(7):
            if (x,y) in rockpos:
                print('#')
            # elif dropping and (x,y) in dropping:
            #     print('@')
            else:
                print('.')
        print('\n')
    print('=============')


def placerock():
    global top
    newtop = -99999999999
    for piece2 in dropping:  # type: ignore
        # Add unmoved pieces
        newtop = max(newtop, piece2[1])
        rockpos.add(piece2)
    dropping = None
    top = max(newtop, top)

while True:
    direction = IN[dir_i % len(IN)]
    if direction == "<":
        offset = -1
    else:
        offset = 1

    # Drop new rock
    if not dropping:
        dropping = rocks[rock_i % len(rocks)]
        rock_i += 1
        new_rock = []
        for piece in dropping:
            # Move 2 units right from left
            piece = (piece[0] + 2, piece[1]) 
            # 3 up from floor/top
            piece = (piece[0], piece[1] + top + 3) 
            new_rock.append(piece)
        dropping = new_rock
        # printboard()

    # Push rock
    new_rock = []
    for piece in dropping:
        bounds = piece[0] + offset
        if bounds not in range(7):
            break
        piece = (piece[0] + offset, piece[1])

        if piece in rockpos:
            # cancel movement
            break
        new_rock.append(piece)
    else:
        # If not out of bounds, move it
        dropping = new_rock

    # Move down
    new_rock = []
    for piece in dropping:
        piece = (piece[0], piece[1] - 1)
        if piece in rockpos:
            # It hit another rock! Can't fall down more
            newtop = -99999999999
            for piece2 in dropping:
                # Add unmoved pieces
                newtop = max(newtop, piece2[1])
                rockpos.add(piece2)
            dropping = None
            top = max(newtop, top)

            # Use ctrl + f to find cycle length
            if top == 501 + 1:
                print("TOOK", rock_i, "TO START CYCLE")
            if top == 501 + 2634 + 1:
                print("TOOK", rock_i, "TO FINISH CYCLE")
            if top == 501 + 2634 * 2 + 1:
                print("TOOK", rock_i, "TO FINISH CYCLE")
            
            if rock_i == 1695 + 204:
                print("REST OF ROCKS", top)

            break
        new_rock.append(piece)
    else:
        dropping = new_rock
    
    dir_i += 1
    # printboard()
    if rock_i == 10_001:
        # print(top)
        break

# printboard()
