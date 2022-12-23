// https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
// 7 kyu
// Reverse words

package kata

import "strings"

// My Solution
func ReverseWords(str string) string {
	words := strings.Split(str, " ")
	wordsLength := len(words)
	result := make([]string, wordsLength)

	for i := 0; i < wordsLength; i++ {
		word := strings.Split(words[i], "")
		var reversed string
		for j := len(word) - 1; j >= 0; j-- {
			reversed += word[j]
		}
		result[i] = reversed
	}
	return strings.Join(result, " ")
}

// Codewars Solution
func ReverseWords2(str string) string {
	var rev string
	var word string

	for _, i := range str {
		if i == ' ' {
			rev = rev + word + " "
			word = ""
		} else {
			word = string(i) + word
		}
	}

	return rev + word
}
