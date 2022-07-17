#include <stdio.h>

int main(void) {
	int num;
	scanf("%d", &num);
	if (num <= 100000) {
		for (int i = 1; i <= num; i++) {
			printf("%d\n", i);
		}
	}
	else
		printf("숫자를 다시 입력하세요.");

			return 0;

}