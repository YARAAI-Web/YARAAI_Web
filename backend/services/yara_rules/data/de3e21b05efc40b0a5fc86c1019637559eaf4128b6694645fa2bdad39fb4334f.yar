rule auto_rule_20250726112441_3261 {
  strings:
    $o0 = "dword_463898" wide ascii nocase
    $o1 = "copy_start" wide ascii nocase
    $o2 = "main_loop_entrance" wide ascii nocase
  condition:
    3 of ($o*)
}