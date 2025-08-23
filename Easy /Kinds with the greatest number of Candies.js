/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    let res = [];
    let maxCandies = Math.max(...candies); // Calculate max once
    
    for (let x of candies) {
        // Check if the current child can have the most candies
        res.push(x + extraCandies >= maxCandies);
    }
  
    return res;
};
