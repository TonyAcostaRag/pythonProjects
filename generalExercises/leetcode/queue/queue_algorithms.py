
def wallsAndGates(rooms: list[list[int]]) -> None:
        
    EMPTY_ROOM = 2147483647
    GATE = 0
    direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    empty_rooms_found = []

    queue = []
    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] == GATE:
                queue.append((row, col))

    while len(queue) > 0:

        point = queue.pop(0)
        empty_rooms_found.append(point)
        row = point[0]
        col = point[1]
        for dir in direction:
            r = row + dir[0]
            c = col + dir[1]
            if r >= len(rooms) or c >= len(rooms[0]) or r < 0 or c < 0 or rooms[r][c] != EMPTY_ROOM:
                continue
            rooms[r][c] = rooms[row][col] + 1
            queue.append((r, c))

    for point in empty_rooms_found:
        print(point, end=' -> ')
    print()
    
def numIslands_BFS_approach(grid: list[list[str]]) -> int:
        
    m = len(grid)
    n = len(grid[0])
    point_visited = set()
    queue = []
    total_islands = 0
    
    def island_explorer_BFS(queue: list, grid: list[list[str]], point_visited: set) -> None:
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while len(queue) > 0:
            point = queue.pop(0)
            row = point[0]
            col = point[1]
            for direction in directions:
                
                r = row + direction[0]
                c = col + direction[1]
                if r >= m or c >= n or r < 0 or c < 0 or grid[r][c] != '1' or (r, c) in point_visited:
                    continue

                queue.append((r, c))
                point_visited.add((r, c))
        
    for row in range(m):
        for col in range(n):
            
            if (row, col) in point_visited:
                continue
            
            if grid[row][col] == '1':
                total_islands += 1
                queue.append((row, col))
                point_visited.add((row, col))
                island_explorer_BFS(queue, grid, point_visited)
    
    return total_islands

def timeRequiredToBuy(tickets: list[int], k: int) -> int:

    secs_elapsed = 0

    while True:
        if tickets[0] == 1:
            tickets.pop(0)
            if k == 0:
                break
        else:
            tickets[0] -= 1
            tickets.append(tickets.pop(0))
        
        secs_elapsed += 1
        k -= 1
        if k < 0:
            k = len(tickets)-1
    secs_elapsed += 1
    return secs_elapsed

def countStudents_n2(students: list[int], sandwiches: list[int]) -> int:

    sandwiches_set = set(sandwiches)
    students_set = set(students)
    while students and (
        sandwiches_set.issubset(students_set) or 
        (students_set.issubset(sandwiches_set) and sandwiches[0] == students[0])
    ):

        if sandwiches[0] == students[0]:
            students.pop(0)
            sandwiches.pop(0)
        else:
            students.append(students.pop(0))

        sandwiches_set = set(sandwiches)
        students_set = set(students)
    return len(students)

def countStudents(students: list[int], sandwiches: list[int]) -> int:

    reject_student = 0
    while students and reject_student < len(students):

        if sandwiches[0] == students[0]:
            students.pop(0)
            sandwiches.pop(0)
            reject_student = 0
        else:
            students.append(students.pop(0))
            reject_student += 1

    return len(students)


if __name__ == '__main__':
    
    '''
    # walls and gates
    rooms = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647]
    ]
    wallsAndGates(rooms)
    for rows in rooms:
        for room in rows:
            print(room, end=' | ')
        print()
    '''

    '''
    # num of Islands
    test_inputs = [ 
        [[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]],
        [[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]]
    ]
    expected_result = [
        1, 3
    ]
    for i in range(len(test_inputs)):
        result = numIslands_BFS_approach(*test_inputs[i])
        if result == expected_result[i]:
            print('PASSED')
        else:
            print('FAILED', 'Actual:', result, 'Expected:', expected_result[i])
    '''

    '''
    # timeRequiredToBuy
    test_inputs = [ 
        [[2,3,2], 2],
        [[5,1,1,1], 0]
    ]
    expected_result = [
        6, 8
    ]
    for i in range(len(test_inputs)):
        result = timeRequiredToBuy(*test_inputs[i])
        if result == expected_result[i]:
            print('PASSED')
        else:
            print('FAILED', 'Actual:', result, 'Expected:', expected_result[i])
    '''

    
    # countStudentsUnableToEau
    test_inputs = [ 
        [[1,1,0,0], [0,1,0,1]],
        [[1,1,1,0,0,1], [1,0,0,0,1,1]],
        [[1,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,1], [0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0]],
        [[0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,1], [1,0,0,0,0,0,0,1,0,0,1,0,1,1,1,0]]
    ]
    expected_result = [
        0,  
        3,
        3, 
        1
    ]
    for i in range(len(test_inputs)):
        result = countStudents(*test_inputs[i])
        if result == expected_result[i]:
            print('PASSED')
        else:
            print('FAILED', 'Actual:', result, 'Expected:', expected_result[i])
    
