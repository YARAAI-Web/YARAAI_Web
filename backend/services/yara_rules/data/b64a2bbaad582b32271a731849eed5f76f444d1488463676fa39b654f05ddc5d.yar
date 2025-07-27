rule auto_rule_20250726112714_4374 {
  strings:
    $o0 = "off_45D91C" wide ascii nocase
  condition:
    all of them
}