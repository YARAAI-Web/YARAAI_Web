rule auto_rule_20250726193829_4685 {
  strings:
    $o0 = "GetClassNameA" wide ascii nocase
    $o1 = "FileA" wide ascii nocase
    $o2 = "DlgDirSelectExA" wide ascii nocase
    $o3 = "hwndClient" wide ascii nocase
  condition:
    4 of ($o*)
}