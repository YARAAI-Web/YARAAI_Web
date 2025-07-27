rule auto_rule_20250726204627_3438 {
  strings:
    $o0 = "off_44D56C" wide ascii nocase
    $o1 = "x30000" wide ascii nocase
  condition:
    all of them
}