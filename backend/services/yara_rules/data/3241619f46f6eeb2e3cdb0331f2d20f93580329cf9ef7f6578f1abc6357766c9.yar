rule auto_rule_20250726173628_1642 {
  strings:
    $o0 = "byte_4123E8" wide ascii nocase
  condition:
    all of them
}