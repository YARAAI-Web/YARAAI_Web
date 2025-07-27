rule auto_rule_20250726222538_4903 {
  strings:
    $o0 = "psSource" wide ascii nocase
  condition:
    all of them
}