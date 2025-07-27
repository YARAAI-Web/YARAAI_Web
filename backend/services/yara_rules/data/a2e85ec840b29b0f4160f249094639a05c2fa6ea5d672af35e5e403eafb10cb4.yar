rule auto_rule_20250726194635_2598 {
  strings:
    $o0 = "RtlImageDirectoryEntryToData" wide ascii nocase
    $o1 = "dword_78148" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}