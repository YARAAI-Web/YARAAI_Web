rule auto_rule_20250726204349_2906 {
  strings:
    $o0 = "dword_44B65C" wide ascii nocase
    $o1 = "TrailDown2" wide ascii nocase
    $o2 = "tail_loop_start" wide ascii nocase
    $o3 = "dword_44BE64" wide ascii nocase
  condition:
    4 of ($o*)
}