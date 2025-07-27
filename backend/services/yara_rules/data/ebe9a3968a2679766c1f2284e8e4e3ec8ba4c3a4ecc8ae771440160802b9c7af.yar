rule auto_rule_20250726112241_2363 {
  strings:
    $o0 = "copy_tail_loop" wide ascii nocase
    $o1 = "byte_411A30" wide ascii nocase
    $o2 = "dword_412268" wide ascii nocase
    $o3 = "dword_411D68" wide ascii nocase
  condition:
    4 of ($o*)
}