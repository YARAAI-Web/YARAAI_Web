rule auto_rule_20250726171641_5584 {
  strings:
    $o0 = "dword_467E90" wide ascii nocase
    $o1 = "main_loop_entrance" wide ascii nocase
  condition:
    all of them
}