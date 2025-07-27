rule auto_rule_20250726201942_6090 {
  strings:
    $o0 = "off_44DD14" wide ascii nocase
    $o1 = "main_loop_entrance" wide ascii nocase
    $o2 = "off_44DD2C" wide ascii nocase
  condition:
    3 of ($o*)
}