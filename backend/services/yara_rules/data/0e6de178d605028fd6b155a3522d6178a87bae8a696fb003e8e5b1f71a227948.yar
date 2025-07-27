rule auto_rule_20250727043052_1668 {
  strings:
    $o0 = "off_429296" wide ascii nocase
  condition:
    all of them
}