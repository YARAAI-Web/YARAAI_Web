rule auto_rule_20250726120018_8008 {
  strings:
    $o0 = "off_44BF70" wide ascii nocase
    $o1 = "main_loop_start" wide ascii nocase
    $o2 = "tail_loop_start" wide ascii nocase
    $o3 = "dword_44C8E4" wide ascii nocase
  condition:
    4 of ($o*)
}