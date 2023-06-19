#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node;

struct List {
	struct Node *head;
	int size;
};

struct Node {
	int data;
	struct Node *next;
};

struct Node create_node(int val) {
	struct Node node;
	node.data = val;
	return (node);
}

void change_node_value(struct Node *node, int value) {
	node->data = value;
}

void add_node(struct List *list, int value) {
	// Add value to linked list
	// List empty (no head) add new head, make val for that head
	// If not keep traversing until node.next == null and make node.next new node with val
}

void remove_node(struct List *list, int index) {
	// Search for index provided
	// If index is last item, simply set previous.next == null
	// If index is in middle, set previous.next to curr.next and free that node
	// If index not found, simply do nothing
}

void print_list_contents(struct List *list) {
	// Print each node in a list
	// While current node is not empty, print and move on
	// Do this until node is null
}

/* Implement linked list struct */
int main() {
	struct List linkedlist;

	return 0;
}

void node_test() {
	struct Node node;
	node.data = 15;
	printf("First value: %d \n", node.data);
	change_node_value(&node, 25);
	printf("Second value: %d \n", node.data);
}
