rule auto_rule_20250726063620_6615 {
  strings:
    $o0 = "flsall" wide ascii nocase
    $o1 = "dword_4642A4" wide ascii nocase
  condition:
    all of them
}