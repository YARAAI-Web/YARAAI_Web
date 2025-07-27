rule auto_rule_20250726170753_7381 {
  strings:
    $o0 = "lpszCurrent" wide ascii nocase
    $o1 = "lopen" wide ascii nocase
  condition:
    all of them
}