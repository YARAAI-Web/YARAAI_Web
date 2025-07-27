rule auto_rule_20250726141622_2480 {
  strings:
    $o0 = "dword_64031464" wide ascii nocase
  condition:
    all of them
}