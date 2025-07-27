rule auto_rule_20250726162611_1166 {
  strings:
    $o0 = "dword_402FA0" wide ascii nocase
  condition:
    all of them
}