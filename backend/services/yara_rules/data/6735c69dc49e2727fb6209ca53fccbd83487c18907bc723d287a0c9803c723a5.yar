rule auto_rule_20250726200118_2207 {
  strings:
    $o0 = "off_46E008" wide ascii nocase
  condition:
    all of them
}