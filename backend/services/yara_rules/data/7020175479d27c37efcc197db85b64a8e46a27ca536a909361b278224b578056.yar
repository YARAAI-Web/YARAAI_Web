rule auto_rule_20250726180126_3387 {
  strings:
    $o0 = "x17000u" wide ascii nocase
    $o1 = "x4016D0" wide ascii nocase
    $o2 = "GetWindowsDirectoryW" wide ascii nocase
  condition:
    3 of ($o*)
}