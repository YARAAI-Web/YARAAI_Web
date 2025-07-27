rule auto_rule_20250726202710_6292 {
  strings:
    $o0 = "x244ECB9Cu" wide ascii nocase
  condition:
    all of them
}