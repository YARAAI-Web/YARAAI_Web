rule auto_rule_20250727032854_7688 {
  strings:
    $o0 = "qword_1400203D8" wide ascii nocase
    $o1 = "ymm1" wide ascii nocase
  condition:
    all of them
}