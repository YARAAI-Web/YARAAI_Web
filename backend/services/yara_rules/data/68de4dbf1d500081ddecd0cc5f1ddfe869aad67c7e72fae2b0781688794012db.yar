rule auto_rule_20250726075600_2441 {
  strings:
    $o0 = "dword_47F240" wide ascii nocase
  condition:
    all of them
}