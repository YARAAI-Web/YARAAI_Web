rule auto_rule_20250727035523_2151 {
  strings:
    $o0 = "EnumDisplaySettingsA" wide ascii nocase
    $o1 = "idAttach" wide ascii nocase
    $o2 = "GetMonitorInfoA" wide ascii nocase
  condition:
    3 of ($o*)
}