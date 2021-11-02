package main

import (
	"fmt"
	"os"
	"sort"
	"strings"
)

func main() {
	dat, err := os.ReadFile("./names.txt")
	if err != nil {
		panic(err)
	}

	names := strings.Split(
		strings.ReplaceAll(string(dat), "\"", ""),
		",")

	sort.Strings(names)

	finalCount := 0
	for i, name := range names {
		score := toScore(name)
		finalCount += score * (i + 1)
	}
	fmt.Printf("%d", finalCount)
}
func toScore(s string) int {
	score := 0
	for _, char := range s {
		score += toScoreChar(char)
	}
	return score
}

func toScoreChar(c rune) int {
	return int(c - 'A' + 1)
}
