#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* insert_node - Function inserts a number into a sorted singly linked list.
* @head: A pointer to a pointer to the start of the linked list
* @number: The data to be inserted
* Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *node = malloc(sizeof(listint_t));

	if (node == NULL)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (temp == NULL || temp->n >= node->n)
	{
		node->next = temp;
		temp = node;
	}
	else
	{
		while (temp->next != NULL && temp->next->n < node->n)
			temp = temp->next;
		node->next = temp->next;
		temp->next = node;
	}
	return (temp);
}
