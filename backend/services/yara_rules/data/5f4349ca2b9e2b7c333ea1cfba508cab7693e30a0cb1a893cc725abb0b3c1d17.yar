rule auto_rule_20250726225826_6566 {
  strings:
    $o0 = "dword_401BE4" wide ascii nocase
  condition:
    all of them
}