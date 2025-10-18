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
var performInOrderTraversal = function (node, list) {
    if (node == null) {
        return;
    }
    performInOrderTraversal(node.left, list);
    list.push(node.val);
    performInOrderTraversal(node.right, list);
};

var buildBinarySearchTree = function (list, start, end) {
    if (start > end) {
        return null;
    }
    
    let mid = Math.floor(start + (end - start) / 2);
    let root = new TreeNode(list[mid]);
    root.left = buildBinarySearchTree(list, start, mid - 1);
    root.right = buildBinarySearchTree(list, mid + 1, end);

    return root;
};

var balanceBST = function (root) {
    let list = [];
    performInOrderTraversal(root, list);
    let start = 0;
    let end = list.length - 1;
    return buildBinarySearchTree(list, start, end);
};
