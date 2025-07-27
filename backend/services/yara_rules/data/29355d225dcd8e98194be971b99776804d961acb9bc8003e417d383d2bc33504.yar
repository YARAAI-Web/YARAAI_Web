rule auto_rule_20250726095155_1695 {
  strings:
    $o0 = "x54354u" wide ascii nocase
    $o1 = "GetMenuStringA" wide ascii nocase
  condition:
    all of them
}