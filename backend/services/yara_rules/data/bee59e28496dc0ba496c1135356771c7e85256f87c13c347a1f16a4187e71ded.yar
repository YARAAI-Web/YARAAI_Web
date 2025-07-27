rule auto_rule_20250726133939_0990 {
  strings:
    $o0 = "byte_409179" wide ascii nocase
  condition:
    all of them
}