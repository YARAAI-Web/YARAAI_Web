rule auto_rule_20250726151518_6438 {
  strings:
    $o0 = "dword_411D40" wide ascii nocase
    $o1 = "old_esp" wide ascii nocase
    $o2 = "DrawDibEnd" wide ascii nocase
    $o3 = "dword_4119AC" wide ascii nocase
  condition:
    4 of ($o*)
}