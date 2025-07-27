rule auto_rule_20250726225247_5085 {
  strings:
    $o0 = "dword_64030350" wide ascii nocase
  condition:
    all of them
}