rule auto_rule_20250727011655_1631 {
  strings:
    $o0 = "xB9409u" wide ascii nocase
  condition:
    all of them
}