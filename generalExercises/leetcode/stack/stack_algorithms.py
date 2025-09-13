from dataStructures.Linear.stack.Stack import Stack_LinkedList
import huge_input_data


def is_balanced_parentheses(parentheses_input):
    
    open_parenthesis_stack = Stack_LinkedList()
    
    for i in range(len(parentheses_input)):
        
        if (i == 0 or open_parenthesis_stack.height == 0) and parentheses_input[i] == ')':
            return False
        
        elif parentheses_input[i] == '(':
            open_parenthesis_stack.push(parentheses_input[i])
            
        elif open_parenthesis_stack.height > 0 and parentheses_input[i] == ')':
            open_parenthesis_stack.pop()
    
    if open_parenthesis_stack.height == 0:
        return True
    else: 
        return False

def reverse_string(string):
    
    char_stack = Stack_LinkedList()
    for char in string:
        char_stack.push(char)
        
    reverse_string = ''
    while char_stack.height > 0:
        node = char_stack.pop()
        reverse_string += node.value
        
    return reverse_string

def sort_stack_prev(unsorted_stack):
    
    sorted_stack = Stack_LinkedList()
    while not unsorted_stack.is_empty():
        item = unsorted_stack.pop()
        
        while not sorted_stack.is_empty() and sorted_stack.peek() and sorted_stack.peek().value > item.value:
            top_item = sorted_stack.pop()
            unsorted_stack.push(top_item.value)
            
        sorted_stack.push(item.value)

    while not sorted_stack.is_empty():
        item = sorted_stack.pop()
        unsorted_stack.push(item.value)

def sort_stack(unsorted_stack):

    sorted_stack = Stack_LinkedList()
    while not unsorted_stack.is_empty():
        node = unsorted_stack.pop()

        while not sorted_stack.is_empty() and sorted_stack.peek().value > node.value:
            unsorted_stack.push(sorted_stack.pop().value)
        
        sorted_stack.push(node.value)

    while not sorted_stack.is_empty():
        unsorted_stack.push(sorted_stack.pop().value)

def removeDuplicates(s: str) -> str:

    char_stack = []
    for char in s:

        if char_stack and char == char_stack[-1]:
            char_stack.pop()
        else:
            char_stack.append(char)

    return ''.join(char_stack)

def backspaceCompare_space(s: str, t: str) -> bool:

    s_stack = []
    for c in s:

        if c == '#':
            if s_stack:
                s_stack.pop()
        else:
            s_stack.append(c)

    s_string = ''.join(s_stack)

    t_stack = []
    for c in t:

        if c == '#':
            if t_stack:
                t_stack.pop()
        else:
            t_stack.append(c)

    t_string = ''.join(t_stack)

    if len(s_string) == len(t_string):
        for i in range(len(t_string)):
            if s_string[i] != t_string[i]:
                return False
        return True
    else:
        return False

def reverseParentheses(s: str) -> str:

    stack_str = []
    i = 0
    inner_str = ''
    while i < len(s):

        temp_str = ''
        # Llenar la pila
        if s[i] == '(':
            stack_str.append(inner_str)
            i += 1
            while s[i] != ')' and s[i] != '(':
                temp_str += s[i]
                i += 1
            inner_str = temp_str
        elif s[i] == ')':
            # Reversear el string dentro de los parentesis (inner_str).
            reversed_str = ''
            for char in reversed(inner_str):
                reversed_str += char
            inner_str = stack_str[-1] + reversed_str
            stack_str.pop()
            i += 1
        else:
            inner_str += s[i]
            i += 1
    
    return inner_str

def reverseParenthesis_WormholeJumpTech(s: str) -> str:

    paired_indexes = [0] * len(s)
    open_parenthesis_stack = []
    for i in range(len(s)):

        if s[i] == '(':
            open_parenthesis_stack.append(i)
        if s[i] == ')':
            j = open_parenthesis_stack.pop()
            paired_indexes[i] = j
            paired_indexes[j] = i
    
    direction = 1
    currIndex = 0
    result = ''
    for i in range(len(s)):

        if s[currIndex] == '(' or s[currIndex] == ')':
            currIndex = paired_indexes[currIndex]
            direction = -direction
        else:
            result += s[currIndex]
        
        currIndex += direction

    return result

def removeOuterParentheses(s: str) -> str:

    open_parenthesis_stack = []
    paired_indexes = [0] * len(s)
    for i in range(len(s)):

        if s[i] == '(':
            open_parenthesis_stack.append(i)

        elif s[i] == ')':

            if len(open_parenthesis_stack) > 1:
                open_parenthesis_stack.pop()
            else:
                paired_indexes[i] = 1
                j = open_parenthesis_stack.pop()
                paired_indexes[j] = 1
    
    result = ''
    for i in range(len(s)):

        if paired_indexes[i] == 0:
            result += s[i]

    return result

def finalPrices_n2(prices: list[int]) -> list[int]:

    answer = []
    for i in range(len(prices)):
        discount = 0
        price = prices[i]
        if i < len(prices) - 1:
            j = i+1
            while j < len(prices) and prices[j] > prices[i]:
                j += 1
        
            if j < len(prices) and prices[j] <= prices[i]:
                discount = prices[j]

        answer.append(price-discount)
    
    return answer

def finalPrices(prices: list[int]) -> list[int]:
    
    monotonic_incremental_stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if i < len(prices)-1 and prices[i+1] > prices[i]:
            monotonic_incremental_stack.append(i)
            continue

        if i < len(prices)-1:
            answer[i] = prices[i] - prices[i+1]
            
            while monotonic_incremental_stack and prices[i+1] <= prices[monotonic_incremental_stack[-1]]:
                price_index = monotonic_incremental_stack.pop()
                answer[price_index] = prices[price_index] - prices[i+1]
        else:
            answer[i] = prices[i]
    
    while monotonic_incremental_stack:
        left_index = monotonic_incremental_stack.pop()
        answer[left_index] = prices[left_index]

    return answer

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    
    total_days = len(temperatures)
    monotonic_stack = []
    answer = [0] * total_days
    for i in range(total_days):
        
        while monotonic_stack and temperatures[i] > temperatures[monotonic_stack[-1]]:
            day = monotonic_stack.pop()
            answer[day] = i - day
        monotonic_stack.append(i)

    return answer

def evalRPN(tokens: list[str]) -> int:
    stack = []
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b)
    }
    for token in tokens:
        
        if token not in operations:
            stack.append(int(token))
        else:

            num2 = stack.pop()
            num1 = stack.pop()
            stack.append(operations[token](num1, num2))
    
    return stack.pop()

def numIslands_DFS_approach(grid: list[list[str]]) -> int:
    
    m = len(grid)
    n = len(grid[0])
    elements_array = []
    visited_points = set()
    num_of_islands = 0

    def islandExplorer_DFS(stack: list, grid: list[list[str]], visited: set) -> None:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(stack) > 0:
            point = stack.pop()
            row = point[0]
            col = point[1]
            for direction in directions:
                r = row + direction[0]
                c = col + direction[1]
                if r >= m or c >= n or r < 0 or c < 0 or grid[r][c] != '1' or (r, c) in visited:
                    continue
                visited.add((r, c))
                stack.append((r, c))

    for row in range(m):
        for col in range(n):

            if (row, col) in visited_points:
                continue

            if grid[row][col] == '1':
                num_of_islands += 1
                visited_points.add((row, col))
                elements_array.append((row, col))
                islandExplorer_DFS(elements_array, grid, visited_points)

    return num_of_islands

def makeGood(s: str) -> str:

    stack = []
    for char in s:
        
        if stack and char != stack[-1] and (char.lower() == stack[-1] or char.upper() == stack[-1]):
            stack.pop()
        else:
            stack.append(char)
    
    return ''.join(stack)


if __name__ == '__main__':
    
    '''  
    # Is balance parenthesis tests
    expected_results = [True, True, True, False, False, False, True, True, True, True, False]
    Test_cases = ['((()))', '()', '(()())', '(()', '())', 
                  ')(', '', '()()()()', '(())(())', '(()()())', '((())']

    for i in range(len(expected_results)):
        
        result = is_balanced_parentheses(Test_cases[i])
        if result == expected_results[i]:
            print('TC', i+1, '- PASSED')
        else:
             print('TC', i+1, '- FAILED')
    '''

    '''
    # Reverse string tests.
    expected_results = ['DESSAP', 'LECNAC']
    test_cases = ['PASSED', 'CANCEL']
    for i in range(len(expected_results)):

        result = reverse_string(test_cases[i])
        if result == expected_results[i]:
            print('TC', i+1, '- PASSED')
        else:
             print('TC', i+1, '- FAILED')
    '''

    '''
    # Sorted stack
    unsorted_stack = Stack_LinkedList()
    unsorted_stack.push(3)
    unsorted_stack.push(1)
    unsorted_stack.push(5)
    unsorted_stack.push(4)
    unsorted_stack.push(2)
    unsorted_stack.display_nodes()
    sort_stack(unsorted_stack)
    unsorted_stack.display_nodes()
    '''

    '''
    # Remove adjacent duplicates
    #original_string = "abbaca"
    #original_string = "aababaab"
    #original_string = "aaaaaaaa"
    original_string = huge_input_data.huge_string_with_duplicates_chars
    modified_string = removeDuplicates(original_string)
    print(modified_string)
    '''

    '''
    # Backspace compare

    # Hay otro approach con space complexity = O(1)

    test_inputs = [["ab#c", "ad#c"], ["ab##", "c#d#"], ["a#c", "b"]]
    expected_results = [True, True, False]

    for i in range(len(test_inputs)):
        result = backspaceCompare(*test_inputs[i])
        if result == expected_results[i]:
            print('TC', i+1, '- PASSED')
        else:
            print('TC', i+1, '- FAILED')
    '''

    '''
    # Reverse parenthesis
    tests_inputs = [["(abcd)"], ["(u(love)i)"], ["(ed(et(oc))el)"]]
    expected_results = ["dcba", "iloveu", "leetcode"]

    for i in range(len(tests_inputs)):

        #result = reverseParentheses(*tests_inputs[i])
        result = reverseParenthesis_WormholeJumpTech(*tests_inputs[i])
        if result == expected_results[i]:
            print('TC', i+1, '- PASSED - Result:', result, 'Expected:', expected_results[i])
        else:
            print('TC', i+1, '- FAILED - Result:', result, 'Expected:', expected_results[i])
    '''

    '''
    # Remove outer parenthesis
    tests_inputs = [["(()())(())"], ["(()())(())(()(()))"], ["()()"], ["((()())(()()))"]]
    expected_results = ["()()()", "()()()()(())", "", "(()())(()())"]

    for i in range(len(tests_inputs)):

        result = removeOuterParentheses(*tests_inputs[i])
        if result == expected_results[i]:
            print('TC', i+1, '- PASSED - Result:', result, 'Expected:', expected_results[i])
        else:
            print('TC', i+1, '- FAILED - Result:', result, 'Expected:', expected_results[i])
    
    #print(removeOuterParentheses("((()())(()()))"))
    '''

    '''
    # Final prices
    tests_inputs = [[[8,4,6,2,3]], [[1,2,3,4,5]], [[10,1,1,6]]]
    expected_results = [[4,2,4,2,3], [1,2,3,4,5], [9,0,1,6]]

    for i in range(len(tests_inputs)):

        result = finalPrices(*tests_inputs[i])
        if result == expected_results[i]:
            print('TC', i+1, '- PASSED - Result:', result)
        else:
            print('TC', i+1, '- FAILED - Result:', result, 'Expected:', expected_results[i])
    '''

    '''
    # Daily temperatures
    test_inputs = [ [[73,74,75,71,69,72,76,73]], [[30,40,50,60]], [[30,60,90]] ]
    expected_results = [[1,1,4,2,1,1,0,0], [1,1,1,0], [1,1,0]]

    for i in range(len(test_inputs)):

        result = dailyTemperatures(*test_inputs[i])
        if result == expected_results[i]:
            print('TC', i+1, 'PASSED')
        else:
            print('TC', i+1, 'FAILED - Expected:', expected_results[i], '- Actual:', result)
    '''

    '''
    # Reverse Polish Notation
    test_inputs = [
        [["2","1","+","3","*"]], 
        [["4","13","5","/","+"]],
        [["10","6","9","3","+","-11","*","/","*","17","+","5","+"]],
        [["4","-2","/","2","-3","-","-"]]
    ]
    expected_results = [9, 6, 22, -7]
    for i in range(len(test_inputs)):
        result = evalRPN(*test_inputs[i])
        
        if result == expected_results[i]:
            print('TC', i+1, ': PASSED', sep='')
        else:
            print('TC', i+1, ': FAILED - Expected:', expected_results[i], '- Actual:', result, sep='')
    '''

    '''
    # num of Islands
    test_inputs = [ 
        #[[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]],
        [[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]]
    ]
    expected_result = [
        #1, 
        3
    ]
    for i in range(len(test_inputs)):
        result = numIslands_DFS_approach(*test_inputs[i])
        if result == expected_result[i]:
            print('PASSED')
        else:
            print('FAILED', 'Actual:', result, 'Expected:', expected_result[i])
    '''


    # Good string 
    test_inputs = [ 
        ["Pp"],
        ["leEeetcode"]
    ]
    expected_result = [
        "", 
        "leetcode"
    ]
    for i in range(len(test_inputs)):
        result = makeGood(*test_inputs[i])
        if result == expected_result[i]:
            print('PASSED')
        else:
            print('FAILED', 'Actual:', result, 'Expected:', expected_result[i])

