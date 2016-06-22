#include <stdio.h>

main() {
        int i = 0;
        int a[2];
        a[0] = 10;
        a[1] = 10;
	printf("hello, world\n");
        a[i] = i++; // a[1] == 0
	printf("a[0] = %d, a[1] = %d\n", a[0], a[1]);
        
}

