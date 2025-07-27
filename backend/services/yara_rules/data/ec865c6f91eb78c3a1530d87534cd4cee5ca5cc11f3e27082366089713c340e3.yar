rule auto_rule_20250726113618_3150 {
  strings:
    $o0 = "_mtdeletelocks" wide ascii nocase
    $o1 = "dword_45DABC" wide ascii nocase
    $o2 = "wsprintfA" wide ascii nocase
    $o3 = "dword_45DEF8" wide ascii nocase
    $o4 = "dwInfoType" wide ascii nocase
  condition:
    4 of ($o*)
}