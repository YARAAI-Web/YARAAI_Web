rule auto_rule_20250726071422_2851 {
  strings:
    $o0 = "main_loop_entrance" wide ascii nocase
    $o1 = "__sbh_alloc_new_group" wide ascii nocase
    $o2 = "x41161D" wide ascii nocase
  condition:
    3 of ($o*)
}