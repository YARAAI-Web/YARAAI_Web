rule auto_rule_20250726205418_8709 {
  strings:
    $o0 = "strcat" wide ascii nocase
    $o1 = "dword_410000" wide ascii nocase
    $o2 = "memcpy_0" wide ascii nocase
    $o3 = "finish_loop" wide ascii nocase
  condition:
    4 of ($o*)
}