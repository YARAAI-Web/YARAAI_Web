rule auto_rule_20250726075009_1669 {
  strings:
    $o0 = "off_483854" wide ascii nocase
  condition:
    all of them
}