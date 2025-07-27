rule auto_rule_20250726171306_3272 {
  strings:
    $o0 = "dword_43F020" wide ascii nocase
    $o1 = "lpszTitle" wide ascii nocase
  condition:
    all of them
}