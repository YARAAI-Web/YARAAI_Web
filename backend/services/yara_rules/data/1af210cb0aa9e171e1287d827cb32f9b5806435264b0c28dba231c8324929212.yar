rule auto_rule_20250727040135_5215 {
  strings:
    $o0 = "constPropSheetPagePointer" wide ascii nocase
    $o1 = "off_413BDE" wide ascii nocase
    $o2 = "off_413A5E" wide ascii nocase
    $o3 = "off_433757" wide ascii nocase
  condition:
    4 of ($o*)
}