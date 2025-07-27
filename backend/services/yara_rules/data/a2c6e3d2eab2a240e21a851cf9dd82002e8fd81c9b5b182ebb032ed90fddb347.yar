rule auto_rule_20250726132210_0266 {
  strings:
    $o0 = "dword_41DBE0" wide ascii nocase
    $o1 = "XAmount" wide ascii nocase
  condition:
    all of them
}