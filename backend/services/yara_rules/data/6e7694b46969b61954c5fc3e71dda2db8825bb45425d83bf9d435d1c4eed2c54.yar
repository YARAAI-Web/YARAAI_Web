rule auto_rule_20250726104000_8406 {
  strings:
    $o0 = "dword_1E52C" wide ascii nocase
  condition:
    all of them
}