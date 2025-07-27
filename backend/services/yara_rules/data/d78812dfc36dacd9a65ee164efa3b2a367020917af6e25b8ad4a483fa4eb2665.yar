rule auto_rule_20250726190119_6065 {
  strings:
    $o0 = "GetPrivateProfileSectionNamesA" wide ascii nocase
    $o1 = "dwFileOffsetLow" wide ascii nocase
    $o2 = "nBar" wide ascii nocase
  condition:
    3 of ($o*)
}