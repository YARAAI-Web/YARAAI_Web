rule auto_rule_20250726081016_7690 {
  strings:
    $o0 = "xE0000222" wide ascii nocase
    $o1 = "Service" wide ascii nocase
  condition:
    all of them
}