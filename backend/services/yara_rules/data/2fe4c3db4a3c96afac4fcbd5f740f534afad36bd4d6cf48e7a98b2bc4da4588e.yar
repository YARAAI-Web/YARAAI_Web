rule auto_rule_20250726193249_0118 {
  strings:
    $o0 = "dword_4657D8" wide ascii nocase
    $o1 = "nFile" wide ascii nocase
  condition:
    all of them
}