rule auto_rule_20250726163319_1475 {
  strings:
    $o0 = "x41C4u" wide ascii nocase
    $o1 = "dword_449AC0" wide ascii nocase
    $o2 = "dword_44A3AC" wide ascii nocase
    $o3 = "main_loop_entrance_0" wide ascii nocase
  condition:
    4 of ($o*)
}