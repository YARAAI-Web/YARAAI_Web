rule auto_rule_20250726202234_2468 {
  strings:
    $o0 = "hostlonga" wide ascii nocase
  condition:
    all of them
}