rule auto_rule_20250726205821_2545 {
  strings:
    $o0 = "_global_unwind2" wide ascii nocase
    $o1 = "byte_447E30" wide ascii nocase
    $o2 = "main_loop_0" wide ascii nocase
    $o3 = "dword_462F78" wide ascii nocase
  condition:
    4 of ($o*)
}