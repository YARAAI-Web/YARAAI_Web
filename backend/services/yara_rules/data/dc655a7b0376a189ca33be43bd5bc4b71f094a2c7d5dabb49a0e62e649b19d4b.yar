rule auto_rule_20250726164830_8980 {
  strings:
    $o0 = "dword_449AC8" wide ascii nocase
    $o1 = "main_loop_entrance" wide ascii nocase
    $o2 = "GetStringTypeA" wide ascii nocase
    $o3 = "byte_449600" wide ascii nocase
  condition:
    4 of ($o*)
}