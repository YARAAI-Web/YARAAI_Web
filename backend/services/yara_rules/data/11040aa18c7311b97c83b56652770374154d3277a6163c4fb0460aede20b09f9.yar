rule auto_rule_20250726212437_9293 {
  strings:
    $o0 = "j__free" wide ascii nocase
    $o1 = "dword_6402F990" wide ascii nocase
    $o2 = "x4924923u" wide ascii nocase
    $o3 = "lpOverlapped" wide ascii nocase
  condition:
    4 of ($o*)
}