rule auto_rule_20250726120802_1904 {
  strings:
    $o0 = "nMaxPos" wide ascii nocase
    $o1 = "hsz2" wide ascii nocase
    $o2 = "lpszHelp" wide ascii nocase
    $o3 = "lstrcpyW" wide ascii nocase
  condition:
    4 of ($o*)
}