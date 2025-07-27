rule auto_rule_20250726080811_8847 {
  strings:
    $o0 = "x3477" wide ascii nocase
  condition:
    all of them
}