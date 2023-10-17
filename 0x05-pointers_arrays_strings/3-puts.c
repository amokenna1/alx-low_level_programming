#include "main.h"

/**
 * _puts - prints a string, followed by a new line.
 * @str: input string.
 * Return: no return.
 */
void _puts(char *str)
{
	int cnt = 0;

	while (cnt >= 0)
	{
		if (str[cnt] == '\0')
		{
			_putchar('\n');
			break;
		}
		_putchar(str[cnt]);
		cnt++;
	}
}
