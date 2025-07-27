rule auto_rule_20250726221219_1677 {
  strings:
    $o0 = "PathCompactPathA" wide ascii nocase
    $o1 = "uFiletype" wide ascii nocase
    $o2 = "pszUrl" wide ascii nocase
    $o3 = "EnumDisplaySettingsA" wide ascii nocase
  condition:
    4 of ($o*)
}