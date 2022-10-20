Node *Reverse_ll(Node *head)
{
    if (head == NULL || head->next == NULL)
    {
        return head;
    }
    Node *next = NULL;
    Node *curr = head;
    Node *prev = NULL;
    while (curr != NULL)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}
