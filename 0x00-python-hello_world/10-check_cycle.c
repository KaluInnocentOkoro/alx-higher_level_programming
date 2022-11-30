#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* check_cycle - function checks for cycle in a singly linked list
* @list: A pointer to the start of the linked list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
 int check_cycle(listint_t *list)
{
	listint_t *slow_node = list, *fast_node = list;

	while (slow_node && fast_node && fast_node->next)
	{
		slow_node = slow_node->next;
		fast_node = fast_node->next->next;
		if (slow_node == fast_node)
			return (1);
	}
	return (0);
}
