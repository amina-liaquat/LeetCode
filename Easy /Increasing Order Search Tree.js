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
var increasingBST = function(root) {
    let dummy = new TreeNode(-1);
    let curr = dummy;
    function inorder(node) {
        if (node === null) return;
        inorder(node.left);
        node.left = null;     // left null kar diya
        curr.right = node;    // list me attach kiya
        curr = node;          // curr ko update kiya
        inorder(node.right);
    };
    inorder(root);
    return dummy.right;
};
