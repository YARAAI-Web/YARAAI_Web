rule auto_rule_20250726145044_1565 {
  strings:
    $o0 = "dword_1EFC0" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}