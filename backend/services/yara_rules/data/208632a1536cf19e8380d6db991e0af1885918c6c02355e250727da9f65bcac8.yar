rule auto_rule_20250726111128_1586 {
  strings:
    $o0 = "program" wide ascii nocase
    $o1 = "dword_412224" wide ascii nocase
    $o2 = "TargetIp" wide ascii nocase
    $o3 = "copy_tail_loop" wide ascii nocase
    $o4 = "dword_40E000" wide ascii nocase
  condition:
    4 of ($o*)
}