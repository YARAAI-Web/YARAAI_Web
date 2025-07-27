rule auto_rule_20250726210843_1689 {
  strings:
    $o0 = "dwLowBytesToSeek" wide ascii nocase
  condition:
    all of them
}