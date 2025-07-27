rule auto_rule_20250726101846_6878 {
  strings:
    $o0 = "tail_loop_start_0" wide ascii nocase
    $o1 = "gu_return" wide ascii nocase
    $o2 = "TrailUp0_0" wide ascii nocase
    $o3 = "dword_4771C8" wide ascii nocase
  condition:
    4 of ($o*)
}