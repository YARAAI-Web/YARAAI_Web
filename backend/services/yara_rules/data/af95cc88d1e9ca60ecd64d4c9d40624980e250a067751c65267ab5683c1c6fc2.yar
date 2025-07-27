rule auto_rule_20250726231453_8154 {
  strings:
    $o0 = "x59CDu" wide ascii nocase
  condition:
    all of them
}