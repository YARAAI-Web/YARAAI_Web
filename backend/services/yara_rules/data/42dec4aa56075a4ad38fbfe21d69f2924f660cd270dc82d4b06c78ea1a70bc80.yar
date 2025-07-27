rule auto_rule_20250726224208_1422 {
  strings:
    $o0 = "_wincmdln" wide ascii nocase
    $o1 = "dword_449EAC" wide ascii nocase
    $o2 = "dword_44A020" wide ascii nocase
    $o3 = "dword_44A3B0" wide ascii nocase
  condition:
    4 of ($o*)
}