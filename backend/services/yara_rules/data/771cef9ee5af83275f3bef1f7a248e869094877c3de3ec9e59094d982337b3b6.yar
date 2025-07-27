rule auto_rule_20250726193010_7052 {
  strings:
    $o0 = "Sourcea" wide ascii nocase
    $o1 = "dword_463B08" wide ascii nocase
    $o2 = "fflush" wide ascii nocase
    $o3 = "_wincmdln" wide ascii nocase
  condition:
    4 of ($o*)
}