rule auto_rule_20250726184404_0118 {
  strings:
    $o0 = "fdwDetails" wide ascii nocase
    $o1 = "TrailUp0_0" wide ascii nocase
    $o2 = "tail_loop_start" wide ascii nocase
    $o3 = "dword_463A24" wide ascii nocase
  condition:
    4 of ($o*)
}