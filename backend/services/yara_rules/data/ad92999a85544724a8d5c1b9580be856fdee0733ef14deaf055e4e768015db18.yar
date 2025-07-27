rule auto_rule_20250726122521_6999 {
  strings:
    $o0 = "aEsdMin94Fi4y" wide ascii nocase
    $o1 = "dword_413BFE" wide ascii nocase
    $o2 = "szLongPath" wide ascii nocase
    $o3 = "FileAttributes" wide ascii nocase
  condition:
    4 of ($o*)
}