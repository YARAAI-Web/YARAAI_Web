rule auto_rule_20250726173618_4127 {
  strings:
    $o0 = "x3498AAF8" wide ascii nocase
  condition:
    all of them
}