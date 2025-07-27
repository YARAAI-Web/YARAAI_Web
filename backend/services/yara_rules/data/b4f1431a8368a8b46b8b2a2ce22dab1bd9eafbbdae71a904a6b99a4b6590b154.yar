rule auto_rule_20250726210050_7515 {
  strings:
    $o0 = "tail_loop_start_0" wide ascii nocase
    $o1 = "_heap_init" wide ascii nocase
    $o2 = "dword_46ED64" wide ascii nocase
    $o3 = "x412A75" wide ascii nocase
  condition:
    4 of ($o*)
}