rule auto_rule_20250727012901_0108 {
  strings:
    $o0 = "__sbh_resize_block" wide ascii nocase
    $o1 = "tail_loop_start_0" wide ascii nocase
    $o2 = "dword_45CEF4" wide ascii nocase
  condition:
    3 of ($o*)
}