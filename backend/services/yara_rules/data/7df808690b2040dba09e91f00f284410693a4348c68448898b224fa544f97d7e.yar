rule auto_rule_20250727030123_2585 {
  strings:
    $o0 = "x6458" wide ascii nocase
    $o1 = "aCelXwhb" wide ascii nocase
  condition:
    all of them
}