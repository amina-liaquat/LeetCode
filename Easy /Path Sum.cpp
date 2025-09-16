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
    bool hasPathSum(TreeNode* root, int targetSum) {
        if( root == nullptr){
            return false;
        }

        stack<TreeNode*> path;
        stack<int> sumPath;

        path.push(root);
        sumPath.push(root -> val);

        while(!path.empty()){
            TreeNode* temp = path.top();
            path.pop();
            int tempVal = sumPath.top();
            sumPath.pop();

            if (temp -> left == nullptr && temp -> right == nullptr && tempVal == targetSum){
                return true;
            }

            if (temp -> right != nullptr){
                path.push (temp -> right);
                sumPath.push(tempVal + temp -> right -> val);
            }

            if (temp -> left != nullptr){
                path.push(temp -> left);
                sumPath.push(tempVal + temp -> left -> val);
            }
        }
        return false;
    }
};






