rule auto_rule_20250726185133_1477 {
  strings:
    $o0 = "dword_405594" wide ascii nocase
    $o1 = "dword_4055FC" wide ascii nocase
  condition:
    all of them
}