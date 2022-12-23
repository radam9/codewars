// https://www.codewars.com/kata/56dbe0e313c2f63be4000b25
// 7 kyu
// Moves in squared strings (I)

package kata

import "strings"

// My Solution

func split(s string) []string {
  return strings.Split(s, "\n")
}

func join(s []string) string {
  return strings.Join(s, "\n")
}

func VertMirror(s string) string {
  groups := split(s)
  for a, group := range groups {
    runes := []rune(group)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
      runes[i], runes[j] = runes[j], runes[i]
    }
    groups[a] = string(runes)
  }
  return join(groups)
}

func HorMirror(s string) string {
  groups := split(s)
  items := len(groups)
  for i := 0; i < items/2; i++ {
    temp := groups[items-1-i]
    groups[items-1-i] = groups[i]
    groups[i] = temp
  }
  return join(groups)
}

type FParam func(string) string

func Oper(f FParam, x string) string {
  return f(x)
}

// Codewars Solution
func revstring(s string) string {
  var u = make([]byte, len(s))
  copy(u, s)
  for i, j := 0, len(u)-1; i < j; i, j = i+1, j-1 {
          u[i], u[j] = u[j], u[i]
  }
  return string(u)
}
func revarray(s [] string) [] string {
  for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
      s[i], s[j] = s[j], s[i]
  }
  return s
}
func VertMirror(s string) string {
  arr := strings.Split(s, "\n")
  var res = []string{}
  for i := 0; i < len(arr); i++ {
      res = append(res, revstring(arr[i]))
  }
  return strings.Join(res, "\n")
}
func HorMirror(s string) string {
  arr := strings.Split(s, "\n")
  revarray(arr)
  return strings.Join(arr, "\n")
}
type FParam func(string) string
func Oper(f FParam, x string) string {
  return f(x)
}
