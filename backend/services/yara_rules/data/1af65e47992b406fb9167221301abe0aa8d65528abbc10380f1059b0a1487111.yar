rule auto_rule_20250726201021_9355 {
  strings:
    $o0 = "TrailUp0_0" wide ascii nocase
    $o1 = "dword_41150C" wide ascii nocase
    $o2 = "dword_411960" wide ascii nocase
    $o3 = "GetStringTypeA" wide ascii nocase
    $o4 = "start_byte_3" wide ascii nocase
  condition:
    4 of ($o*)
}