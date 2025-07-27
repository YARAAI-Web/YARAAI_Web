rule auto_rule_20250726105907_6334 {
  strings:
    $o0 = "CodePagea" wide ascii nocase
    $o1 = "byte_40DCC0" wide ascii nocase
  condition:
    all of them
}