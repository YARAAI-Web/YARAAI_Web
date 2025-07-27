rule auto_rule_20250726135059_8898 {
  strings:
    $o0 = "dword_469B9C" wide ascii nocase
  condition:
    all of them
}