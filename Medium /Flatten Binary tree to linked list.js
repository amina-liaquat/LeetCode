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
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function (root) {
    let dummyNode = new TreeNode(-1);
    let ptr = dummyNode;

    let dfs = function (node) {
        if (node === null) return;

        let left = node.left;
        let right = node.right;

        ptr.right = node;
        ptr.left = null;
        ptr = node;

        dfs(left);
        dfs(right);
    }

    dfs(root);
    return dummyNode.right;
};
