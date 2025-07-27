rule auto_rule_20250726194859_5254 {
  strings:
    $o0 = "hostlonga" wide ascii nocase
  condition:
    all of them
}