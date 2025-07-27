rule auto_rule_20250727030432_5049 {
  strings:
    $o0 = "off_48385C" wide ascii nocase
  condition:
    all of them
}