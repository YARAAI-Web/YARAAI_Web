rule auto_rule_20250726154014_9833 {
  strings:
    $o0 = "lpszDesktop" wide ascii nocase
    $o1 = "GetDCEx" wide ascii nocase
    $o2 = "x17000u" wide ascii nocase
    $o3 = "lpnLengthNeeded" wide ascii nocase
  condition:
    4 of ($o*)
}