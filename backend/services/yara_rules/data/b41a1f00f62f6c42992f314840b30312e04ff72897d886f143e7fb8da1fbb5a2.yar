rule auto_rule_20250726173437_4684 {
  strings:
    $o0 = "byte_64028DEC" wide ascii nocase
  condition:
    all of them
}