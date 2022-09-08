#include <stdio.h>
int main(void) {
	int i = 0,num;
	
	scanf("%d", &num);
	
	for (i = num; i > 0; i--) {
		printf("%d\n", i);
	}

	return 0;
}
