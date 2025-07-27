rule auto_rule_20250727040106_4940 {
  strings:
    $o0 = "_snprintf" wide ascii nocase
    $o1 = "byte_4642BC" wide ascii nocase
  condition:
    all of them
}