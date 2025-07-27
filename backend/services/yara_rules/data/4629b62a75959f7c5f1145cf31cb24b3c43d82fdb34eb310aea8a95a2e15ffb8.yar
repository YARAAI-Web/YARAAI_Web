rule auto_rule_20250727024632_4125 {
  strings:
    $o0 = "dword_456D00" wide ascii nocase
  condition:
    all of them
}