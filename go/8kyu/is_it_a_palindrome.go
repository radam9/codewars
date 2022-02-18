// https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
// 8 kyu
// Is it a palindrome?

package kata

import "strings"

// My Solution
func IsPalindrome(str string) bool {
	str = strings.ToLower(str)
	for i := 0; i < (len(str) / 2); i++ {
		j := len(str) - 1 - i
		if str[i] != str[j] {
			return false
		}
	}
	return true
}
