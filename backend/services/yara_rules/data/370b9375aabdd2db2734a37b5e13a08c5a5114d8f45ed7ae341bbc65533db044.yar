rule auto_rule_20250727043128_0914 {
  strings:
    $o0 = "EF0h" wide ascii nocase
    $o1 = "dword_6402E568" wide ascii nocase
  condition:
    all of them
}