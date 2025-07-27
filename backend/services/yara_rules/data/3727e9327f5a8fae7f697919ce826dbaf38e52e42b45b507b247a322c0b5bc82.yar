rule auto_rule_20250726114359_7775 {
  strings:
    $o0 = "dword_42EEA8" wide ascii nocase
    $o1 = "dword_42EECC" wide ascii nocase
  condition:
    all of them
}