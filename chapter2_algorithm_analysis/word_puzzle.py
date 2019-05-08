
def left(puzzle, word, i, j):
    sneak = j
    for letter in word:
        if sneak < 0:
            return None
        if letter != puzzle[i][sneak]:
            return None
        sneak -= 1
    return (word, i, j, i, sneak)

def right(puzzle, word, i, j):
    sneak = j
    cols = len(puzzle[i])
    for letter in word:
        if sneak >= cols:
            return None
        if letter != puzzle[i][sneak]:
            return None
        sneak += 1
    return (word, i, j, i, sneak)

def up(puzzle, word, i, j):
    sneak = i
    for letter in word:
        if sneak < 0:
            return None
        if letter != puzzle[sneak][j]:
            return None
        sneak -= 1
    return (word, i, j, sneak, j)

def down(puzzle, word, i, j):
    sneak = i
    rows = len(puzzle)
    for letter in word:
        if sneak >= rows:
            return None
        if letter != puzzle[sneak][j]:
            return None
        sneak += 1
    return (word, i, j, sneak, j)

def left_up(puzzle, word, i, j):
    sneak_x = i
    sneak_y = j
    for letter in word:
        if sneak_x < 0 or sneak_y < 0:
            return None
        if letter != puzzle[sneak_x][sneak_y]:
            return None
        sneak_x -= 1
        sneak_y -= 1
    return (word, i, j, sneak_x, sneak_y)

def right_up(puzzle, word, i, j):
    sneak_x = i
    sneak_y = j
    cols = len(puzzle[i])
    for letter in word:
        if sneak_x < 0 or sneak_y >= cols:
            return None
        if letter != puzzle[sneak_x][sneak_y]:
            return None
        sneak_x -= 1
        sneak_y += 1
    return (word, i, j, sneak_x, sneak_y)

def left_down(puzzle, word, i, j):
    sneak_x = i
    sneak_y = j
    rows = len(puzzle)
    for letter in word:
        if sneak_x >= rows or sneak_y < 0:
            return None
        if letter != puzzle[sneak_x][sneak_y]:
            return None
        sneak_x += 1
        sneak_y -= 1
    return (word, i, j, sneak_x, sneak_y)

def right_down(puzzle, word, i, j):
    sneak_x = i
    sneak_y = j
    rows = len(puzzle)
    cols = len(puzzle[i])
    for letter in word:
        if sneak_x >= rows or sneak_y >= cols:
            return None
        if letter != puzzle[sneak_x][sneak_y]:
            return None
        sneak_x += 1
        sneak_y += 1
    return (word, i, j, sneak_x, sneak_y)

def brute1(puzzle, words):
    for word in words:
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                solutions = [
                    left(puzzle, word, i, j),
                    right(puzzle, word, i, j),
                    up(puzzle, word, i, j),
                    down(puzzle, word, i, j),
                    left_up(puzzle, word, i, j),
                    right_up(puzzle, word, i, j),
                    left_down(puzzle, word, i, j),
                    right_down(puzzle, word, i, j)
                ]
                solutions = list(filter(lambda s : s, solutions))
                if solutions:
                    break
            if solutions:
                break
        if solutions:
            for solution in solutions:
                w, ii, jj, x, y = solution
                print("{} is from [{},{}] to [{},{}]".format(w, ii, jj, x, y))

def test():
    puzzle = [
        ['t', 'h', 'i', 's'],
        ['w', 'a', 't', 's'],
        ['o', 'a', 'h', 'g'],
        ['f', 'g', 'd', 't']
    ]
    words = ['this', 'two', 'fat', 'that']
    brute1(puzzle, words)

test()
                    
                    