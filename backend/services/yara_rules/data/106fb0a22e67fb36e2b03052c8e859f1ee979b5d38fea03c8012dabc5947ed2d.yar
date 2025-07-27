rule auto_rule_20250726112904_5026 {
  strings:
    $o0 = "byte_4BB500" wide ascii nocase
  condition:
    all of them
}