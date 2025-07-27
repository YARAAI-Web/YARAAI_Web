rule auto_rule_20250726112042_5555 {
  strings:
    $o0 = "tail_loop_start_0" wide ascii nocase
    $o1 = "dword_44C40C" wide ascii nocase
    $o2 = "_heap_alloc" wide ascii nocase
  condition:
    3 of ($o*)
}