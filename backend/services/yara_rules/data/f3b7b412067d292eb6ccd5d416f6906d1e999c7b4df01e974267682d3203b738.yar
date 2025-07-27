rule auto_rule_20250726123302_4398 {
  strings:
    $o0 = "Handler" wide ascii nocase
    $o1 = "dword_4663A0" wide ascii nocase
    $o2 = "_abnormal_termination" wide ascii nocase
    $o3 = "x423DA5" wide ascii nocase
    $o4 = "main_loop_entrance" wide ascii nocase
  condition:
    4 of ($o*)
}