rule auto_rule_20250726160911_6089 {
  strings:
    $o0 = "aGnxwmou" wide ascii nocase
  condition:
    all of them
}