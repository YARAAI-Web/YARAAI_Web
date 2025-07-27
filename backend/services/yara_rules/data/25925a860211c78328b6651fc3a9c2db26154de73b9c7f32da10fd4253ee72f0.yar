rule auto_rule_20250726225850_4731 {
  strings:
    $o0 = "lpFindFileData" wide ascii nocase
    $o1 = "GetProfileSectionW" wide ascii nocase
    $o2 = "uSize" wide ascii nocase
    $o3 = "CancelWaitableTimer" wide ascii nocase
  condition:
    4 of ($o*)
}