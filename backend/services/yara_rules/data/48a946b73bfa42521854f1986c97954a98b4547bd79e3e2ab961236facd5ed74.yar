rule auto_rule_20250726172222_5818 {
  strings:
    $o0 = "GetStringTypeA" wide ascii nocase
    $o1 = "byte_45FEC0" wide ascii nocase
  condition:
    all of them
}