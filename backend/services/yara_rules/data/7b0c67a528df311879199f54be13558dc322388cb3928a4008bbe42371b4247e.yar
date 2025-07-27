rule auto_rule_20250726231331_3460 {
  strings:
    $o0 = "dword_476E08" wide ascii nocase
    $o1 = "dword_476E10" wide ascii nocase
  condition:
    all of them
}