rule auto_rule_20250727010101_1038 {
  strings:
    $o0 = "dword_434603" wide ascii nocase
  condition:
    all of them
}