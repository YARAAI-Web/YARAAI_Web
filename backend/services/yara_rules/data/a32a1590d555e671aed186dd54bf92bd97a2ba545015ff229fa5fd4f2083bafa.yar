rule auto_rule_20250727000954_3700 {
  strings:
    $o0 = "byte_4C127C" wide ascii nocase
  condition:
    all of them
}