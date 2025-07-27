rule auto_rule_20250726162246_0785 {
  strings:
    $o0 = "dword_45FE00" wide ascii nocase
    $o1 = "dword_447020" wide ascii nocase
    $o2 = "main_loop_0" wide ascii nocase
  condition:
    3 of ($o*)
}