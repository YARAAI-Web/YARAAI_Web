rule auto_rule_20250726183827_7727 {
  strings:
    $o0 = "_abnormal_termination" wide ascii nocase
    $o1 = "memcpy_0" wide ascii nocase
    $o2 = "main_loop_1" wide ascii nocase
    $o3 = "dword_410AB4" wide ascii nocase
    $o4 = "TrailUp0_0" wide ascii nocase
  condition:
    5 of ($o*)
}