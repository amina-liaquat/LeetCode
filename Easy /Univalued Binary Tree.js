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
var isUnivalTree = function (root) {
    // let compare = (root, val) => {
    //     if (root == null) {
    //         return true;
    //     };
    //     if (root.val != val) {
    //         return false;
    //     };
    //     let left = compare(root.left, val);
    //     let right = compare(root.right, val);
    //     return left && right;
    // };
    // return compare(root, root.val);

    // Itterative Approach
    if (root == null){
        return true;
    }

    let val = root.val;
    let stack = [root];
    while (stack.length > 0){
        let poppedNode = stack.pop();
        if(poppedNode.val != val){
            return false;
        }
        if(poppedNode.left){
            stack.push(poppedNode.left);
        }
        if(poppedNode.right){
            stack.push(poppedNode.right);
        }
    }

    return true;
};
