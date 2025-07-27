rule auto_rule_20250726164544_1867 {
  strings:
    $o0 = "SetUserObjectInformationW" wide ascii nocase
    $o1 = "SetWindowsHookA" wide ascii nocase
    $o2 = "GetShellWindow" wide ascii nocase
  condition:
    3 of ($o*)
}