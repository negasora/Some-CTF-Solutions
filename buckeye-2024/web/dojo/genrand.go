package main

import (
	"math/rand/v2"
	"fmt"
	"flag"
)

const MaxBossHealth = 1000

func main() {
	var gameId = flag.Int("id", 1234, "game id")
	var bossHealth = flag.Int("health", 1000, "boss health")
	flag.Parse()

	s2 := rand.NewPCG(uint64(*gameId), 1024)
	r2 := rand.New(s2)

    file, err := os.Open("state.txt")
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
		//TODO: for each
        fmt.Println(scanner.Text())
    }

    if err := scanner.Err(); err != nil {
        log.Fatal(err)
    }

	s2.

	v := r2.IntN(100)
	fmt.Println(v)

	if v < 20 {
		if *bossHealth < MaxBossHealth*0.8 {
			randAmt := r2.IntN(50)
			fmt.Println(randAmt)
		} else {
			randAmt := r2.IntN(30)
			fmt.Println(randAmt)
		}
	} else if v < 35 {
		randAmt := r2.IntN(50)
		fmt.Println(randAmt)
	} else if v < 50 {
		randAmt := r2.IntN(30)
		fmt.Println(randAmt)
	}
}
