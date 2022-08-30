#include <stdio.h>
#include <stdlib.h>

int main () {
    int *pont;
    int i;
    pont = (int*)calloc(30*sizeof(int));
    for (i = 0;  i < 30, i++){
    pont[i] = i*2;}
    pont = (int*)realloc(22*sizeof(int));
    free(): void free(void *ptr);
    return 0;
}
