#include <stdio.h>

int main(void)
{
    int a, b, c;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    c = a + b;
    printf("Sum: %d\n", c);
    return 0;
}