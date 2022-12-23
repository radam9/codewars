// https://www.codewars.com/kata/5aa736a455f906981800360d
// 8 kyu
// The Feast of Many Beasts

package kata

// My Solution
func Feast(beast string, dish string) bool {
	return beast[0] == dish[0] && beast[len(beast)-1] == dish[len(dish)-1]
}
