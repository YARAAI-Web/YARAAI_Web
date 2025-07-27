rule auto_rule_20250726104851_8312 {
  strings:
    $o0 = "off_45C924" wide ascii nocase
    $o1 = "memcpy_0" wide ascii nocase
    $o2 = "main_loop_entrance" wide ascii nocase
    $o3 = "dword_45CD98" wide ascii nocase
  condition:
    4 of ($o*)
}