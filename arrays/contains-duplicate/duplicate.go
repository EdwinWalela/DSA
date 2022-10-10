package main

import "fmt"

func containsDuplicate(nums []int) bool {

	hash_map := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		currVal, exists := hash_map[nums[i]]
		if exists {
			return true
		} else {
			hash_map[nums[i]] = currVal + 1
		}
	}
	return false
}

func main() {
	list := []int{1, 2, 3, 4, 5}
	fmt.Println(containsDuplicate((list)))
}
