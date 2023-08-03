class Solution(object):
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if self.search(board, word, r, c, 0, visited):
                    return True
        return False

    def search(self, board, word, r, c, L, visited):
        if L == len(word):
            return True

        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or visited[r][c] or board[r][c] != word[L]:
            return False

        visited[r][c] = True
        found = (
            self.search(board, word, r + 1, c, L + 1, visited)
            or self.search(board, word, r - 1, c, L + 1, visited)
            or self.search(board, word, r, c + 1, L + 1, visited)
            or self.search(board, word, r, c - 1, L + 1, visited)
        )
        visited[r][c] = False

        return found
