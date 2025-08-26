/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head || !head->next || k == 0) return head;
        ListNode* curr = head;
        int len = 1;
        while (curr->next) {
            len++;
            curr = curr->next;
        }
        k = k % len;
        if (k == 0) return head;
        curr->next = head; //Make circular Linked List
        int i = 1;
        while (i <= len - k ) {
            curr = curr->next;
            i++;
        }
        ListNode* new_head = curr->next;
        curr->next = nullptr;
        return new_head;
    }
};
        
