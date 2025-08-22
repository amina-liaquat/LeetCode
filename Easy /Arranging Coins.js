/**
 * @param {number} n
 * @return {number}
 */
var arrangeCoins = function(n) {
  let rows = 0;
    let totalCoins = 0;
    while (totalCoins <= n) {
        rows += 1;
        totalCoins += rows;  
};
 return rows - 1;
}
