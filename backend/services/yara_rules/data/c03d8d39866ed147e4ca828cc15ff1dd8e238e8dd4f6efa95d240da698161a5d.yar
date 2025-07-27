rule auto_rule_20250726165733_2732 {
  strings:
    $o0 = "TerminateThread" wide ascii nocase
    $o1 = "main_loop_1" wide ascii nocase
    $o2 = "off_469534" wide ascii nocase
    $o3 = "dword_469D7C" wide ascii nocase
    $o4 = "joyGetDevCapsA" wide ascii nocase
  condition:
    4 of ($o*)
}