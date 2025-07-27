rule auto_rule_20250726171348_4308 {
  strings:
    $o0 = "crKey" wide ascii nocase
    $o1 = "lpChar" wide ascii nocase
    $o2 = "ChangeDisplaySettingsA" wide ascii nocase
    $o3 = "GetWindowDC" wide ascii nocase
  condition:
    4 of ($o*)
}