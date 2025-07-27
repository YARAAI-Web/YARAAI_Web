rule auto_rule_20250726232708_6303 {
  strings:
    $o0 = "x17000u" wide ascii nocase
    $o1 = "aWmCommand" wide ascii nocase
    $o2 = "GetWindowsDirectoryW" wide ascii nocase
  condition:
    3 of ($o*)
}