#include <errno.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/mman.h>

int main(int argc, char** argv)
{
    if (argc != 2)
    {
        printf("Usage: %s <seed>", argv[0]);
        return 1;
    }

    int seed = atoi(argv[1]);
    if (errno)
    {
        puts("Seed parse failed");
        return 1;
    }

    srand(seed);

    int fd = open("/tmp/mem.bin", O_RDWR|O_CREAT|O_TRUNC, (mode_t)0600);
    lseek(fd, 0x10000000-1, SEEK_SET);
    write(fd, "", 1);
    int* memFile = mmap(0, 0x10000000, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 0);
    for (int i = 0; i < 0x4000000; i++)
    {
        memFile[i] = rand();
    }

    msync(memFile, 0x10000000, MS_SYNC);
    munmap(memFile, 0x10000000);
    close(fd);

    return 0;
}
