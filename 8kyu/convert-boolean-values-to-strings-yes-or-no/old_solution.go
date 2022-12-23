// https://www.codewars.com/kata/53369039d7ab3ac506000467
// 8 kyu
// Convert boolean values to strings 'Yes' or 'No'.

package kata

// My Solution
func BoolToWord(word bool) string {
	if word {
		return "Yes"
	}
	return "No"
}
