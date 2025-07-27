rule auto_rule_20250726224944_0447 {
  strings:
    $o0 = "x41C4u" wide ascii nocase
    $o1 = "byte_411C21" wide ascii nocase
    $o2 = "TargetIp" wide ascii nocase
    $o3 = "dword_411E54" wide ascii nocase
  condition:
    4 of ($o*)
}