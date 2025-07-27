rule auto_rule_20250726114833_1653 {
  strings:
    $o0 = "CharPrevA" wide ascii nocase
    $o1 = "dword_41DB30" wide ascii nocase
    $o2 = "idTransaction" wide ascii nocase
    $o3 = "EnumDisplaySettingsA" wide ascii nocase
  condition:
    4 of ($o*)
}