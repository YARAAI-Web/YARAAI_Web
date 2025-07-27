rule auto_rule_20250726202914_0549 {
  strings:
    $o0 = "dword_44A3B8" wide ascii nocase
    $o1 = "_wincmdln" wide ascii nocase
  condition:
    all of them
}