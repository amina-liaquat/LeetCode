/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function (board) {
    function isValid(row, col, num) {
        for (let i = 0; i < 9; i++) {
            if (board[row][i] === num) return false;
            if (board[i][col] === num) return false;
        }

        const boxRow = 3 * Math.floor(row / 3);
        const boxCol = 3 * Math.floor(col / 3);
        for (let i = boxRow; i < boxRow + 3; i++) {
            for (let j = boxCol; j < boxCol + 3; j++) {
                if (board[i][j] === num) return false;
            }
        }
        return true;
    }

    function solve() {
        // Find the first empty cell
        for (let row = 0; row < 9; row++) {
            for (let col = 0; col < 9; col++) {

                if (board[row][col] === '.') {

                    // Try digits 1–9
                    for (let num = 1; num <= 9; num++) {
                        const char = num.toString();

                        if (isValid(row, col, char)) {
                            board[row][col] = char;

                            if (solve()) return true;

                            board[row][col] = '.';
                        }
                    }

                    // Tried all numbers, none worked → backtrack
                    return false;
                }
            }
        }

        // No empty cell found → solved
        return true;
    }

    solve();
};
