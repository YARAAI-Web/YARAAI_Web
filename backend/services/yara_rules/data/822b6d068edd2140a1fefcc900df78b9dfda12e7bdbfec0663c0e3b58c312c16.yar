rule auto_rule_20250726124617_7109 {
  strings:
    $o0 = "off_4335F8" wide ascii nocase
  condition:
    all of them
}