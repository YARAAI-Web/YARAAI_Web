rule auto_rule_20250726225839_4597 {
  strings:
    $o0 = "dword_42EEA4" wide ascii nocase
    $o1 = "GetWindowsDirectoryW" wide ascii nocase
    $o2 = "dwDesiredAccess" wide ascii nocase
  condition:
    3 of ($o*)
}