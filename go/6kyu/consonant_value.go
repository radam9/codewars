// https://www.codewars.com/kata/59c633e7dcc4053512000073
// 6 kyu
// Consonant value

package kata

// My Solution

var VOWELS = map[rune]bool{'a': true, 'i': true, 'o': true, 'e': true, 'u': true}

func solve(str string) int {
	var current, max int
	for _, letter := range str {
		if !VOWELS[letter] {
			current += int(letter) - 96
			continue
		}
		if current > max {
			max = current
		}
		current = 0
	}
	if current > max {
		return current
	}
	return max
}

// Codewars Solution

func solve(str string) int {
	var sum, max int
	for _, letter := range str {
		switch letter {
		case 'a', 'e', 'i', 'o', 'u':
			sum = 0
			continue
		}
		sum += int(letter) - 96
		if sum > max {
			max = sum
		}
	}
	return max
}
