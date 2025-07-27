rule auto_rule_20250726144026_7483 {
  strings:
    $o0 = "x87312909" wide ascii nocase
  condition:
    all of them
}