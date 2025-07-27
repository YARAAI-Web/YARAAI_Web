rule auto_rule_20250727044244_3772 {
  strings:
    $o0 = "satti" wide ascii nocase
  condition:
    all of them
}