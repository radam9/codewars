//
// 7 kyu
// Make a function that does arithmetic!

package kata

// My Solution
func Arithmetic(a int, b int, operator string) int {
	switch operator {
	case "add":
		return a + b
	case "subtract":
		return a - b
	case "multiply":
		return a * b
	case "divide":
		return a / b
	default:
		panic("Unknown operator")
	}
}
