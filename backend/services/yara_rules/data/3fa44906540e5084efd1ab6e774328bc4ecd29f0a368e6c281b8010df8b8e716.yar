rule auto_rule_20250726155103_5123 {
  strings:
    $o0 = "dword_449018" wide ascii nocase
  condition:
    all of them
}