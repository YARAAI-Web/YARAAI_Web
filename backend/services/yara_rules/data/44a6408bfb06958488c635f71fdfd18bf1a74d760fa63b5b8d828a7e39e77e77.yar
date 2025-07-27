rule auto_rule_20250726150733_6033 {
  strings:
    $o0 = "hostlonga" wide ascii nocase
  condition:
    all of them
}