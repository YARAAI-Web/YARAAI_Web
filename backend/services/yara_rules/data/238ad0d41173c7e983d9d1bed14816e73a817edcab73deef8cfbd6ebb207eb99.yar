rule auto_rule_20250726084741_1627 {
  strings:
    $o0 = "GetDiskFreeSpaceW" wide ascii nocase
    $o1 = "lpCodePageEnumProc" wide ascii nocase
    $o2 = "xCF0000u" wide ascii nocase
    $o3 = "IsWindowUnicode" wide ascii nocase
  condition:
    4 of ($o*)
}