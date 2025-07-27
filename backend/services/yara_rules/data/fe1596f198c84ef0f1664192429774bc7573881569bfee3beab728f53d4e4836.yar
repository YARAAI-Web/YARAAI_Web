rule auto_rule_20250727022813_9550 {
  strings:
    $o0 = "xF89C85D5" wide ascii nocase
  condition:
    all of them
}