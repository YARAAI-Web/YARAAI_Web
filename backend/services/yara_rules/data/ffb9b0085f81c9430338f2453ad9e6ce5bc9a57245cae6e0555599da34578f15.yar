rule auto_rule_20250726212310_7796 {
  strings:
    $o0 = "dword_41E25C" wide ascii nocase
    $o1 = "dword_41E230" wide ascii nocase
    $o2 = "dword_41E3A0" wide ascii nocase
    $o3 = "__sbh_resize_block" wide ascii nocase
    $o4 = "copy_tail_loop" wide ascii nocase
  condition:
    4 of ($o*)
}