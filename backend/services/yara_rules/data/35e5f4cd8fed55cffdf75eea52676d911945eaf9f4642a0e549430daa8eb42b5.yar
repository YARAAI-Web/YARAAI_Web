rule auto_rule_20250726220406_4183 {
  strings:
    $o0 = "x1004u" wide ascii nocase
    $o1 = "found_bx" wide ascii nocase
    $o2 = "_global_unwind2" wide ascii nocase
    $o3 = "xDAE9B268" wide ascii nocase
    $o4 = "main_loop_entrance" wide ascii nocase
  condition:
    5 of ($o*)
}