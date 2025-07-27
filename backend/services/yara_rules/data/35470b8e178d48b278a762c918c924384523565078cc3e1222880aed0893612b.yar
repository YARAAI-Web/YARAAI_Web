rule auto_rule_20250726225412_8640 {
  strings:
    $o0 = "off_465B48" wide ascii nocase
  condition:
    all of them
}