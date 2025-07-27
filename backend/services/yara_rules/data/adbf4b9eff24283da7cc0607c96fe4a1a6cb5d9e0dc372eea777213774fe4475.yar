rule auto_rule_20250726205713_3784 {
  strings:
    $o0 = "EFFh" wide ascii nocase
    $o1 = "GetWindowsDirectoryW" wide ascii nocase
  condition:
    all of them
}