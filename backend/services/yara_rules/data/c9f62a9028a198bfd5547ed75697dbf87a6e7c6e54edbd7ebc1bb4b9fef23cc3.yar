rule auto_rule_20250726155645_4286 {
  strings:
    $o0 = "off_4699F0" wide ascii nocase
    $o1 = "main_loop_entrance" wide ascii nocase
  condition:
    all of them
}