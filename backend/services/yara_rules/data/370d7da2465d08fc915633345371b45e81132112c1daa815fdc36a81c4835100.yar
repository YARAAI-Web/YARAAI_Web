rule auto_rule_20250726070359_0027 {
  strings:
    $o0 = "xFF557508" wide ascii nocase
  condition:
    all of them
}