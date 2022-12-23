// https://www.codewars.com/kata/52685f7382004e774f0001f7
// 5 kyu
// Human Readable Time

package kata

import (
	"fmt"
)

func HumanReadableTime(seconds int) string {
	h := seconds / 3600
	m := (seconds % 3600) / 60
	s := seconds % 60
	return fmt.Sprintf("%02d:%02d:%02d", h, m, s)
}
