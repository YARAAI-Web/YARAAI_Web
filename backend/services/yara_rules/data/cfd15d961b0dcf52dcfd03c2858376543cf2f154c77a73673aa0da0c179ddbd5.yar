rule auto_rule_20250726234459_1442 {
  strings:
    $o0 = "dwInfoType" wide ascii nocase
    $o1 = "VirtualFree" wide ascii nocase
    $o2 = "dword_45CFC0" wide ascii nocase
    $o3 = "dword_45D8B8" wide ascii nocase
  condition:
    4 of ($o*)
}