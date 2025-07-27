rule auto_rule_20250726073600_8818 {
  strings:
    $o0 = "dword_77F94" wide ascii nocase
    $o1 = "dword_77CF0" wide ascii nocase
    $o2 = "dword_77EDC" wide ascii nocase
    $o3 = "dword_77FB4" wide ascii nocase
    $o4 = "init" wide ascii nocase
  condition:
    4 of ($o*)
}