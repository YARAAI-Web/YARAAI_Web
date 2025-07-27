rule auto_rule_20250726101309_6797 {
  strings:
    $o0 = "x103Bu" wide ascii nocase
    $o1 = "_tmpfname" wide ascii nocase
    $o2 = "LibraryA" wide ascii nocase
    $o3 = "_wincmdln" wide ascii nocase
    $o4 = "dword_45AFB8" wide ascii nocase
  condition:
    4 of ($o*)
}