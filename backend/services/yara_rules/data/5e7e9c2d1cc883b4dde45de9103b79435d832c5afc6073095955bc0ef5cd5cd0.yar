rule auto_rule_20250726190409_1492 {
  strings:
    $o0 = "VirtualFreeEx" wide ascii nocase
    $o1 = "dword_45B4B0" wide ascii nocase
    $o2 = "TargetIp" wide ascii nocase
    $o3 = "_ftbuf" wide ascii nocase
  condition:
    4 of ($o*)
}