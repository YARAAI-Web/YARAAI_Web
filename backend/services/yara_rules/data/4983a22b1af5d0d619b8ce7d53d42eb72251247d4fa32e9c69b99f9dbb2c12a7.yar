rule auto_rule_20250726091530_9406 {
  strings:
    $o0 = "GetWindowsDirectoryW" wide ascii nocase
    $o1 = "dword_402F38" wide ascii nocase
  condition:
    all of them
}