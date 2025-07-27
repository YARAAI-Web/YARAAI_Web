rule auto_rule_20250726132955_5432 {
  strings:
    $o0 = "SystemWindowsDirectoryA" wide ascii nocase
    $o1 = "lpMaximumApplicationAddress" wide ascii nocase
    $o2 = "x7F28u" wide ascii nocase
  condition:
    3 of ($o*)
}