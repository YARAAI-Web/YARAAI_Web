rule auto_rule_20250727030218_4089 {
  strings:
    $o0 = "dword_45D7A0" wide ascii nocase
    $o1 = "dword_45CF48" wide ascii nocase
    $o2 = "copy_tail_loop" wide ascii nocase
    $o3 = "main_loop_0" wide ascii nocase
  condition:
    4 of ($o*)
}