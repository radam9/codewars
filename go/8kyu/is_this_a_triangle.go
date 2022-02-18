// https://www.codewars.com/kata/56606694ec01347ce800001b
// 7 kyu
// Is this a triangle?

package kata

// My Solution
func IsTriangle(a, b, c int) bool {
	return (a+b > c) && (a+c > b) && (b+c > a)
}
