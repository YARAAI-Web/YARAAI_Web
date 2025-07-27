rule auto_rule_20250726180526_3651 {
  strings:
    $o0 = "m128i_i8" wide ascii nocase
    $o1 = "TrailDown2" wide ascii nocase
    $o2 = "dword_40A2A0" wide ascii nocase
    $o3 = "byte_401778" wide ascii nocase
  condition:
    4 of ($o*)
}