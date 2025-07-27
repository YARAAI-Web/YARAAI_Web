rule auto_rule_20250726062637_0117 {
  strings:
    $o0 = "dword_4756A8" wide ascii nocase
  condition:
    all of them
}