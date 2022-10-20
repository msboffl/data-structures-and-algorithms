class Solution {
public:
    ListNode* reverse_node(ListNode* head, int k, int len)
{

    if(len < k)
    {
        return head;
    }
	    int count = 0;
    ListNode* curr = head;
    ListNode* prev = NULL;
    ListNode* next = NULL;
    while(curr != NULL && count < k)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
        count++;
    }
	
    head->next = reverse_node(next,k,len-k);
	
    return prev;
}

ListNode* reverseKGroup(ListNode* head, int k) { 
    int len = 0;
    ListNode* temp = head;
    while(temp != NULL)
    {
        len++;
        temp = temp->next;
    }

    temp = head;
	
   return reverse_node(temp,k,len);
    
}
};
