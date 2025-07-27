rule auto_rule_20250726105252_9038 {
  strings:
    $o0 = "dword_45D8B4" wide ascii nocase
    $o1 = "xcptlookup" wide ascii nocase
    $o2 = "_wincmdln" wide ascii nocase
    $o3 = "nProgram" wide ascii nocase
    $o4 = "dword_45D558" wide ascii nocase
  condition:
    4 of ($o*)
}