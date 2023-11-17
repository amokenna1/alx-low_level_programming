#include "lists.h"
/**
 * list_len - returns then number of element in a list.
 * @h: singly linked list.
 * Return: number of elements in the list.
 */

size_t list_len(const list_t *h)
{
	size_t nodeCount = 0;

	while (h != NULL)
	{
		h = h->next;
		nodeCount++;
	}
	return (nodeCount);
}
