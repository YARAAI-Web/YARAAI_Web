rule auto_rule_20250726220200_4429 {
  strings:
    $o0 = "DdeDisconnect" wide ascii nocase
    $o1 = "dword_423160" wide ascii nocase
  condition:
    all of them
}