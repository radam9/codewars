// https://www.codewars.com/kata/57cfdf34902f6ba3d300001e
// 8 kyu
// Sort and Star

package kata

import (
	"sort"
	"strings"
)

// My Solution
func TwoSort(arr []string) string {
	result := arr[0]

	for i := 1; i < len(arr); i++ {
		word := arr[i]
		if strings.Compare(result, word) == 1 {
			result = word
		}
	}
	return strings.Join(strings.Split(result, ""), "***")
}

// Codewars Solution
func TwoSort2(arr []string) string {
	sort.Strings(arr)
	return strings.Join(strings.Split(arr[0], ""), "***")
}
