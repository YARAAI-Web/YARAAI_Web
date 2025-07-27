rule auto_rule_20250727035217_0381 {
  strings:
    $o0 = "dword_42EEAC" wide ascii nocase
    $o1 = "GetWindowsDirectoryW" wide ascii nocase
  condition:
    all of them
}