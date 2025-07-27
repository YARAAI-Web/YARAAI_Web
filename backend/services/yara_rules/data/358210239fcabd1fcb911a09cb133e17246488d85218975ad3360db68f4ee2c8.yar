rule auto_rule_20250726113341_4331 {
  strings:
    $o0 = "dword_463A24" wide ascii nocase
  condition:
    all of them
}