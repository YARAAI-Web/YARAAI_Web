rule auto_rule_20250726120449_8409 {
  strings:
    $o0 = "_abnormal_termination" wide ascii nocase
    $o1 = "main_loop_start" wide ascii nocase
    $o2 = "dword_45F3B4" wide ascii nocase
  condition:
    3 of ($o*)
}