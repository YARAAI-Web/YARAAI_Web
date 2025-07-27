rule auto_rule_20250726120642_8525 {
  strings:
    $o0 = "byte_40710F" wide ascii nocase
  condition:
    all of them
}