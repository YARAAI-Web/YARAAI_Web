rule auto_rule_20250726190539_0642 {
  strings:
    $o0 = "dword_411958" wide ascii nocase
    $o1 = "copy_tail_loop" wide ascii nocase
    $o2 = "x7A00001" wide ascii nocase
    $o3 = "_global_unwind2" wide ascii nocase
  condition:
    4 of ($o*)
}