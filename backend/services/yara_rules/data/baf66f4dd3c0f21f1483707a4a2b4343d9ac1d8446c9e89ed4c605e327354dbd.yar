rule auto_rule_20250726145216_4546 {
  strings:
    $o0 = "dword_477258" wide ascii nocase
  condition:
    all of them
}