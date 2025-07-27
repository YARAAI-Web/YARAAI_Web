rule auto_rule_20250726113842_9208 {
  strings:
    $o0 = "DdeGetLastError" wide ascii nocase
    $o1 = "bErase" wide ascii nocase
    $o2 = "EnumDisplaySettingsA" wide ascii nocase
  condition:
    3 of ($o*)
}