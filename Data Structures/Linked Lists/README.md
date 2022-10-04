
I) Introduction to linked list




I) Introduction to linked list

● A linked list is a linear data structure where each element is a separate object.

● Each element or node of a list is comprising of two items:

○ Data

○ Pointer(reference) to the next node.

● A linked list is a linear data structure, in which the elements are not stored at
contiguous memory locations.

● The first node of a linked list is known as head.

● The last node of a linked list is known as tail.

● The last node has a reference to null.



II) Linked list class: 


class Node {

public :

int data; // to store the data stored

Node *next; // to store the address of next pointer

Node(int data) {

this -> data = data;

next = NULL;

}

};



Note: The first node in the linked list is known as Head pointer and the last node is
referenced as Tail pointer. We must never lose the address of the head pointer as it
references the starting address of the linked list and is, if lost, would lead to losing of the
list.




 There are generally three types of linked list:


● Singly: Each node contains only one link which points to the subsequent node in the
list.


● Doubly: It’s a two-way linked list as each node points not only to the next pointer
but also to the previous pointer.


● Circular: There is no tail node i.e., the next field is never NULL and the next field for
the last node points to the head node.

III) Taking input in list: 



To take input in the user, we need to keep few things in the mind:

● Always use the first pointer as the head pointer.

● When initialising the new pointer the next pointer should always be referenced to
NULL.

● The current node’s next pointer should always point to the next node to connect the
linked list.

