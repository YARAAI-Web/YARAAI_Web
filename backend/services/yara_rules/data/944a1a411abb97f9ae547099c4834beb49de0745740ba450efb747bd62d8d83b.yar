rule auto_rule_20250726200153_4107 {
  strings:
    $o0 = ".packed" wide ascii nocase
    $o1 = "packed" wide ascii nocase
  condition:
    all of them
}