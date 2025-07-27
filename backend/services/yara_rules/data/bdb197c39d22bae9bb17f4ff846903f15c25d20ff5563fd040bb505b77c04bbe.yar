rule auto_rule_20250726104601_1213 {
  strings:
    $o0 = "dword_411AF0" wide ascii nocase
    $o1 = "dword_411AC0" wide ascii nocase
  condition:
    all of them
}