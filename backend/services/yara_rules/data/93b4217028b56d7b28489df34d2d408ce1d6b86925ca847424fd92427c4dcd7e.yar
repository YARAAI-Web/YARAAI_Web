rule auto_rule_20250726061351_9197 {
  strings:
    $o0 = "main_loop_0" wide ascii nocase
    $o1 = "dword_4791E4" wide ascii nocase
    $o2 = "dword_479318" wide ascii nocase
    $o3 = "dword_4791D0" wide ascii nocase
    $o4 = "UnwindUp6_0" wide ascii nocase
  condition:
    4 of ($o*)
}