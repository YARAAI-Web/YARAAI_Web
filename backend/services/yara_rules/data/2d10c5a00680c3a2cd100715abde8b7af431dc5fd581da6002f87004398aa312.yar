rule auto_rule_20250726152632_0731 {
  strings:
    $o0 = "xFFFFEF44" wide ascii nocase
    $o1 = "dword_4D31A4" wide ascii nocase
  condition:
    all of them
}