rule auto_rule_20250726220318_1609 {
  strings:
    $o0 = "dword_41E3AC" wide ascii nocase
    $o1 = "tail_loop_start" wide ascii nocase
    $o2 = "__sbh_resize_block" wide ascii nocase
    $o3 = "dword_41D79C" wide ascii nocase
  condition:
    4 of ($o*)
}