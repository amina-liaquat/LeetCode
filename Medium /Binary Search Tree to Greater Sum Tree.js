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
 * @return {TreeNode}
 */
var bstToGst = function (root) {
    let sum = 0;
    function helper(node) {
        if (node === null) {
            return;
        };

        helper(node.right);
        sum += node.val;
        node.val = sum;
        helper(node.left);
    }
    helper(root);
    return root;
};
