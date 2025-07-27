rule auto_rule_20250726164627_1741 {
  strings:
    $o0 = "_ShrMan" wide ascii nocase
    $o1 = "tail_loop_start" wide ascii nocase
    $o2 = "off_474A58" wide ascii nocase
    $o3 = "dword_475E2C" wide ascii nocase
    $o4 = "main_loop_entrance" wide ascii nocase
  condition:
    4 of ($o*)
}