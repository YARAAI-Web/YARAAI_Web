rule auto_rule_20250726093159_6636 {
  strings:
    $o0 = "vpclmulqdq" wide ascii nocase
    $o1 = "v293" wide ascii nocase
  condition:
    all of them
}