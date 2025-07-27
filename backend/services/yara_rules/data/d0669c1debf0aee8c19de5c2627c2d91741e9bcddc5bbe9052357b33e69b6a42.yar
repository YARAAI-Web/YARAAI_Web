rule auto_rule_20250726202318_0241 {
  strings:
    $o0 = "aHks5A6q8a9H" wide ascii nocase
    $o1 = "_CloseWindowStationCloseWi" wide ascii nocase
    $o2 = "x752E" wide ascii nocase
    $o3 = "dwMemoryLoad" wide ascii nocase
    $o4 = "AddAtomA" wide ascii nocase
  condition:
    4 of ($o*)
}