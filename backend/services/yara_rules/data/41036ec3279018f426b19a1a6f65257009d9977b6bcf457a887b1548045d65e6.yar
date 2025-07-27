rule auto_rule_20250726110605_5658 {
  strings:
    $o0 = "UnwindUp0_0" wide ascii nocase
    $o1 = "main_loop_entrance" wide ascii nocase
    $o2 = "_CrtMemCheckPoint" wide ascii nocase
  condition:
    3 of ($o*)
}