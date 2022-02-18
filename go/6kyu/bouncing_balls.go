// https://www.codewars.com/kata/5544c7a5cb454edb3c000047
// 6 kyu
// Bouncing Balls

package kata

import "math"

// My Solution
func BouncingBall(h, bounce, window float64) int {
	if h <= 0 || window < 0 || window >= h || bounce <= 0 || bounce >= 1 {
		return -1
	}
	count := 1
	h *= bounce
	for h >= window {
		if h > window {
			count += 2
		}
		h *= bounce
	}
	return count
}

// Codewars Solution
func BouncingBall2(h, bounce, window float64) int {
	if h < 0 || bounce <= 0 || 1 <= bounce || h < window {
		return -1
	}

	var count int = -1
	for ; h > window; h *= bounce {
		count += 2
	}

	return count
}

// Codewars Solution recursive
func BouncingBall3(h, bounce, window float64) int {
	if h <= window || bounce <= 0 || bounce >= 1 {
		return -1
	} else {
		return 2 + BouncingBall((h*bounce), bounce, window)
	}
}

// Codewars Solution mathematical
func BouncingBall4(h, bounce, window float64) int {
	if !(h > 0 && 0 < bounce && bounce < 1 && window < h) {
		return -1
	}
	return int(math.Ceil(math.Log(window/h)/math.Log(bounce)))*2 - 1
}
