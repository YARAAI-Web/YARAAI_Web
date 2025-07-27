rule auto_rule_20250726221519_4146 {
  strings:
    $o0 = "x17000u" wide ascii nocase
  condition:
    all of them
}