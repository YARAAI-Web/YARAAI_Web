rule auto_rule_20250726131640_1260 {
  strings:
    $o0 = "dword_4657D8" wide ascii nocase
    $o1 = "_isctype" wide ascii nocase
    $o2 = "dword_464430" wide ascii nocase
    $o3 = "dword_463AD8" wide ascii nocase
  condition:
    4 of ($o*)
}