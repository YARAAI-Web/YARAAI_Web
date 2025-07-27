rule auto_rule_20250726163855_1676 {
  strings:
    $o0 = "main_loop_entrance" wide ascii nocase
    $o1 = "dword_468004" wide ascii nocase
  condition:
    all of them
}