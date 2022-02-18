//
// 7 kyu
// Maximum Length Difference

package kata

// My Solution
func MxDifLg(a []string, b []string) int {
	if len(a) == 0 || len(b) == 0 {
		return -1
	}
	minA, maxA := getMaxAndMinStringLength(a)
	minB, maxB := getMaxAndMinStringLength(b)

	aMinB := maxA - minB
	bMinA := maxB - minA

	if aMinB > bMinA {
		return aMinB
	} else {
		return bMinA
	}
}

func getMaxAndMinStringLength(arr []string) (min, max int) {
	min = len(arr[0])
	max = len(arr[0])
	for i, _ := range arr {
		length := len(arr[i])
		if length > max {
			max = length
		}
		if length < min {
			min = length
		}
	}
	return
}
