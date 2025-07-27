rule auto_rule_20250727040826_2721 {
  strings:
    $o0 = "byte_640287C0" wide ascii nocase
  condition:
    all of them
}