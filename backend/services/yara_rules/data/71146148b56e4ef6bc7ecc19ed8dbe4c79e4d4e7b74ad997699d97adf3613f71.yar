rule auto_rule_20250726204553_3982 {
  strings:
    $o0 = "_global_unwind2" wide ascii nocase
    $o1 = "copy_tail_loop" wide ascii nocase
    $o2 = "dword_40E5A0" wide ascii nocase
    $o3 = "TrailDown1_0" wide ascii nocase
  condition:
    4 of ($o*)
}