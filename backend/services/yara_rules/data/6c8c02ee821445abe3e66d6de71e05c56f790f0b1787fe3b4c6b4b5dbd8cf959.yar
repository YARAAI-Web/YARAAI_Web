rule auto_rule_20250726090738_6132 {
  strings:
    $o0 = "memcpy_0" wide ascii nocase
    $o1 = "dword_44A030" wide ascii nocase
    $o2 = "main_loop_1" wide ascii nocase
    $o3 = "dword_44A2A0" wide ascii nocase
  condition:
    4 of ($o*)
}