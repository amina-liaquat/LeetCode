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
 * @return {boolean}
 */
var isSymmetric = function (root) {
    if (root == null) {
        return true;
    }
    function check(root1, root2) {
        if (root1 == null && root2 === null) {
            return true;
            // return root1 == root2;
        }
        if (root1 == null || root2 == null) {
            return false;
        }
        if (root1.val === root2.val) {
            let left = check(root1.left, root2.right);
            let right = check(root1.right, root2.left);
            return left && right;
        } else {
            return false;
        }
    }
    return check(root.left, root.right);
};
