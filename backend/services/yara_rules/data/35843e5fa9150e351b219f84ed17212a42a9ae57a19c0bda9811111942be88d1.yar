rule auto_rule_20250726095821_9085 {
  strings:
    $o0 = "_nh_malloc" wide ascii nocase
    $o1 = "main_loop_entrance" wide ascii nocase
    $o2 = "dword_44A3AC" wide ascii nocase
  condition:
    3 of ($o*)
}