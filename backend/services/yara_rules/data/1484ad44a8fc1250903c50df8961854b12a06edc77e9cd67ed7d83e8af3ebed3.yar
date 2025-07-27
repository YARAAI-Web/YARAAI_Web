rule auto_rule_20250726120417_5927 {
  strings:
    $o0 = "dword_4C31FC" wide ascii nocase
  condition:
    all of them
}