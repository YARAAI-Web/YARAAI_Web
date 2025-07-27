rule auto_rule_20250726080339_5460 {
  strings:
    $o0 = "x1401EF9EDLL" wide ascii nocase
  condition:
    all of them
}