/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxi = 0;

    int helper(TreeNode* root) {
        if (!root) return 0;

        int lefth = helper(root->left);
        int righth = helper(root->right);

        // Store the maximum path through the root
        maxi = max(maxi, lefth + righth);

        // Return height of current node
        return 1 + max(lefth, righth);
    }

    int diameterOfBinaryTree(TreeNode* root) {
        helper(root);
        return maxi;
    }
};
