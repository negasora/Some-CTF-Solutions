#include <stdio.h>

#define QUOTE_LITERAL() "
#define bctf char* asd = QUOTE_LITERAL()"
int main()
{
    #include "flag.txt"
;
    printf("%s\n", asd);
}
