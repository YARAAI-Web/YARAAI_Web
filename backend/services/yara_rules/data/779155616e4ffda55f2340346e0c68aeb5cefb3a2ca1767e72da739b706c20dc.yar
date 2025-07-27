rule auto_rule_20250726154715_3727 {
  strings:
    $o0 = "szLongPath" wide ascii nocase
    $o1 = "x8BC1u" wide ascii nocase
    $o2 = "dword_42C008" wide ascii nocase
    $o3 = "off_42179E" wide ascii nocase
  condition:
    4 of ($o*)
}