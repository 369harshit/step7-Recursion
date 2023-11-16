def exist(board, word):
    def dfs(board, word, i, j, k):
        if not (0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] != word[k]:
            return False
        
        if k == len(word) - 1:
            return True
        
        temp, board[i][j] = board[i][j], '/'
        res = (dfs(board, word, i + 1, j, k + 1) or
               dfs(board, word, i - 1, j, k + 1) or
               dfs(board, word, i, j + 1, k + 1) or
               dfs(board, word, i, j - 1, k + 1))
        board[i][j] = temp
        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, word, i, j, 0):
                return True

    return False

board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]

word = "ABCCED"
result = exist(board, word)
print(result)  # This will print True, as the word "ABCCED" can be found in the board.

word = "SEE"
result = exist(board, word)
print(result)  # This will print True, as the word "SEE" can be found in the board.

word = "ABCB"
result = exist(board, word)
print(result)  # This will print False, as the word "ABCB" cannot be found in the board.
