class Solution {
    public boolean isValidSudoku(char[][] board) {

        //squares

        for (int i = 0; i < board.length/3; i ++) {
            for (int j = 0; j < board.length/3;j ++) {
                HashSet<Character> h = new HashSet<>();
                for (int a = i * 3; a < (i * 3) + 3; a ++) {
                    for (int b = j * 3; b < (j*3) + 3; b ++) {
                        if (h.contains(board[a][b])) {

                            return false;
                        }
                        if (board[a][b] != '.') {
                            h.add(board[a][b]);
                        }
                        
                    }
                }
            }
        }

        //row
        for (int i = 0; i < board.length; i ++) {
            HashSet<Character> h = new HashSet<>();
            for (char j : board[i]) {
                if (h.contains(j)) {
                    return false;
                }
                if (j != '.') {
                    h.add(j);
                }
            }
        }

        //col

        for (int i = 0; i < board.length; i ++) {
            HashSet<Character> h = new HashSet<>();
            for (int j = 0; j < board.length; j ++) {
                if (h.contains(board[j][i])) {

                    return false;
                }
                if (board[j][i] != '.') {
                    h.add(board[j][i]);
                }
            }
        }
        return true;
    }
}