rule auto_rule_20250727041724_2082 {
  strings:
    $o0 = "byte_640301F3" wide ascii nocase
  condition:
    all of them
}