rule auto_rule_20250726184646_3089 {
  strings:
    $o0 = "x16D" wide ascii nocase
    $o1 = "dword_511760" wide ascii nocase
  condition:
    all of them
}