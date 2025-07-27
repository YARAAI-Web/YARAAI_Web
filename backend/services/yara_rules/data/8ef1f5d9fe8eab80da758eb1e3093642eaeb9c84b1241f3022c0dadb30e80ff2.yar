rule auto_rule_20250726072950_6991 {
  strings:
    $o0 = "dword_401BE0" wide ascii nocase
  condition:
    all of them
}