rule auto_rule_20250726074750_1625 {
  strings:
    $o0 = "byte_64026636" wide ascii nocase
    $o1 = "x4924923u" wide ascii nocase
    $o2 = "FFF4h" wide ascii nocase
  condition:
    3 of ($o*)
}