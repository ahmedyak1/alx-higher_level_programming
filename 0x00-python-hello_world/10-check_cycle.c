#include "lists.h"

/**
 * check_cycle - function checks.
 * @list: point to the start of the item
 *
 *
 * Return: retunr 1 if is cycle else return 0
 */
int check_cycle(listint_t *list)
{
	listint_t *cur, *ck;

	if (list == NULL || list->next == NULL)
		return (0);
	cur = list;
	ck = cur->next;
	
	
	while (cur != NULL && ck->next != NULL && ck->next->next != NULL)
	{
		if (cur == ck)
			return (1);
		cur = cur->next;
		ck = ck->next->next;
	}
	return (0);
}
