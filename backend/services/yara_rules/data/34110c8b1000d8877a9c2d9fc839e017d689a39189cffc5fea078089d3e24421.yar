rule auto_rule_20250726213314_7913 {
  strings:
    $o0 = "dword_64033334" wide ascii nocase
  condition:
    all of them
}