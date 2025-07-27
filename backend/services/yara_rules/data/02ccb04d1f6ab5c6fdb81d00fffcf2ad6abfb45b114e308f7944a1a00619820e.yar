rule auto_rule_20250726225349_0249 {
  strings:
    $o0 = "lpIconName" wide ascii nocase
    $o1 = "x19000u" wide ascii nocase
  condition:
    all of them
}