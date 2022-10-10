package main

import (
	"fmt"
	"regexp"
	"strings"
)

func cleanStr(str string) string {
	reg, _ := regexp.Compile("[^A-Za-z0-9]")
	str = string(reg.ReplaceAll([]byte(str), []byte{}))
	return strings.ToLower(str)
}

func isPalindrome(str string) bool {
	str = cleanStr(str)
	leftPtr := 0
	rightPtr := len(str) - 1

	for leftPtr < rightPtr {
		if str[leftPtr] != str[rightPtr] {
			return false
		} else {
			leftPtr++
			rightPtr--
		}
	}
	return true
}

func main() {
	fmt.Println(isPalindrome("A man, a plan, a canal: Panama"))
}
