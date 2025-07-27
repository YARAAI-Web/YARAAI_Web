rule auto_rule_20250726203245_6375 {
  strings:
    $o0 = "x392B" wide ascii nocase
    $o1 = "x6C40" wide ascii nocase
  condition:
    all of them
}