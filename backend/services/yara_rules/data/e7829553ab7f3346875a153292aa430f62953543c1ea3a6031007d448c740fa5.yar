rule auto_rule_20250726142157_9312 {
  strings:
    $o0 = "TrailDown1_0" wide ascii nocase
    $o1 = "dword_411EC8" wide ascii nocase
    $o2 = "main_loop_1" wide ascii nocase
  condition:
    3 of ($o*)
}