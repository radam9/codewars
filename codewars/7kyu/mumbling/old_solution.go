// https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
// 7 kyu
// Mumbling

package kata

import "strings"

// My Solution
func Accum(s string) string {
	if len(s) == 0 {
		return ""
	}

	s = strings.ToLower(s)
	var result string
	for i, letter := range s {
		if i != 0 {
			result += "-"
		}
		result += generatePart(string(letter), i+1)
	}
	return result
}

func generatePart(letter string, num int) string {
	var result string

	for i := 0; i < num; i++ {
		if i == 0 {
			result += strings.ToUpper(letter)
		} else {
			result += letter
		}
	}
	return result
}

// Codewars Solution
func Accum2(s string) string {
	parts := make([]string, len(s))

	for i, letter := range s {
		parts[i] = strings.Title(strings.Repeat(strings.ToLower(string(letter)), i+1))
	}

	return strings.Join(parts, "-")
}
