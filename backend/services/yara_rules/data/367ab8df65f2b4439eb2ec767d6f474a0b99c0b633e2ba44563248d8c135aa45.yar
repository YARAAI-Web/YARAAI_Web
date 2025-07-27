rule auto_rule_20250726223034_3205 {
  strings:
    $o0 = "dword_6402E990" wide ascii nocase
  condition:
    all of them
}