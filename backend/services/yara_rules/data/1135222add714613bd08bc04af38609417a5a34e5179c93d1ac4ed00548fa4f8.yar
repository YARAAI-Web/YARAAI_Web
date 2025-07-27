rule auto_rule_20250726071905_6812 {
  strings:
    $o0 = "dword_45982C" wide ascii nocase
  condition:
    all of them
}