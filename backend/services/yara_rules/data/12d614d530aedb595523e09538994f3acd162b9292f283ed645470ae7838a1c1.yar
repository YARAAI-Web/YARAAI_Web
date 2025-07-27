rule auto_rule_20250726162859_8154 {
  strings:
    $o0 = "dword_4D31D4" wide ascii nocase
  condition:
    all of them
}