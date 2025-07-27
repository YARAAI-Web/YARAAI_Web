rule auto_rule_20250727040909_2497 {
  strings:
    $o0 = "byte_4BB500" wide ascii nocase
  condition:
    all of them
}