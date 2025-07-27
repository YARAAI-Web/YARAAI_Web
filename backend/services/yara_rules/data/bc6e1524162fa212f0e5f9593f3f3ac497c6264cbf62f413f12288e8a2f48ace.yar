rule auto_rule_20250727000334_2668 {
  strings:
    $o0 = "v288" wide ascii nocase
    $o1 = "var_2C8" wide ascii nocase
  condition:
    all of them
}