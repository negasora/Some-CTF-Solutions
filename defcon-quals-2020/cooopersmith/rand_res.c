#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    time_t t = time(0);
    srand(t);
    // srand(t+2); // if remote
    int rand1 = rand();
    int rand2 = rand();
    printf("%d\n", rand1+rand2);
}
