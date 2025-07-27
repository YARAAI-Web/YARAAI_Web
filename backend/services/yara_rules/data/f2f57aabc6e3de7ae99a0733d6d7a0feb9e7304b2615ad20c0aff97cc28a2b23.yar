rule auto_rule_20250726083626_4000 {
  strings:
    $o0 = "dword_447A1C" wide ascii nocase
    $o1 = "main_loop_entrance" wide ascii nocase
  condition:
    all of them
}