rule auto_rule_20250726231946_8629 {
  strings:
    $o0 = "main_loop_1" wide ascii nocase
    $o1 = "a_env" wide ascii nocase
  condition:
    all of them
}