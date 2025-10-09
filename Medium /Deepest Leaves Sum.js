/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var deepestLeavesSum = function (root) {
    let sum = 0;
    function height(node) {
        if (node == null) {
            return null;
        }
        let lH = height(node.left);
        let rH = height(node.right);
        return Math.max(lH, rH) + 1;
    }

    function helper(node, height) {
        if (node == null) {
            return;
        }

        if (height === 1) {
            sum += node.val;
        }

        helper(node.left, height - 1);
        helper(node.right, height - 1);
    };
    
    let h = height(root);
    helper(root, h);
    return sum;
};
