rule auto_rule_20250726134343_1294 {
  strings:
    $o0 = "dword_449AD8" wide ascii nocase
    $o1 = "_heap_init" wide ascii nocase
    $o2 = "dword_449940" wide ascii nocase
    $o3 = "main_loop_0" wide ascii nocase
  condition:
    4 of ($o*)
}