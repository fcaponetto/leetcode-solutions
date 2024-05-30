# 79. Word Search (28/11/56382)
# Runtime: 33 ms (94.99%) Memory: 16.47 MB (87.40%) 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        # Count characters in the word and the board
        word_dict = Counter(word)
        board_dict = Counter(itertools.chain.from_iterable(board))
        
        # Check if board contains enough letters to form the word
        if any(count > board_dict[char] for char, count in word_dict.items()):
            return False
        
        # Reverse the word if the first character is more frequent than the last
        if board_dict[word[0]] > board_dict[word[-1]]:
            word = word[::-1]


        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in visited):
                return False

            visited.add((r,c))
            res =  (dfs(r, c+1, i+1) or
                    dfs(r, c-1, i+1) or
                    dfs(r-1, c, i+1) or
                    dfs(r+1, c, i+1))
            visited.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False

