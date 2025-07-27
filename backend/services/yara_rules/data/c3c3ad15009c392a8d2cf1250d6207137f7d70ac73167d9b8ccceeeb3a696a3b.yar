rule auto_rule_20250726142934_6276 {
  strings:
    $o0 = "main_loop_start" wide ascii nocase
    $o1 = "strpbrk" wide ascii nocase
    $o2 = "dword_458274" wide ascii nocase
    $o3 = "off_4571B4" wide ascii nocase
  condition:
    4 of ($o*)
}