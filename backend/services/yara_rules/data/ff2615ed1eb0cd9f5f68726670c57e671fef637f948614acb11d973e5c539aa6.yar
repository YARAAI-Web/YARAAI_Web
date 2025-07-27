rule auto_rule_20250726182621_1577 {
  strings:
    $o0 = "dword_A65004" wide ascii nocase
  condition:
    all of them
}