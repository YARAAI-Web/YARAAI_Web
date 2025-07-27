rule auto_rule_20250726080151_7434 {
  strings:
    $o0 = "byte_463AE5" wide ascii nocase
    $o1 = "off_463C2C" wide ascii nocase
  condition:
    all of them
}