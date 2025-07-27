rule auto_rule_20250726181239_1263 {
  strings:
    $o0 = "copy_tail_loop" wide ascii nocase
    $o1 = "dword_45FD84" wide ascii nocase
    $o2 = "_except_handler3" wide ascii nocase
    $o3 = "off_45FD80" wide ascii nocase
  condition:
    4 of ($o*)
}