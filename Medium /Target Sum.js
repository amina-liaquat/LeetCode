/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var findTargetSumWays = function (nums, target) {
    const memo = new Map();

    function solve(i, remaining) { 
        if (i === nums.length) {
            // ternory operator 
            return remaining === 0 ? 1 : 0; 
        }

        const key = i + "," + remaining;

        if (memo.has(key)) {
            return memo.get(key);
        }

        // Choose +
        const add = solve(i + 1, remaining + nums[i]);

        // Choose -
        const subtract = solve(i + 1, remaining - nums[i]);

        const result = add + subtract;
        memo.set(key, result);

        return result;
    }

    return solve(0, target);
};
