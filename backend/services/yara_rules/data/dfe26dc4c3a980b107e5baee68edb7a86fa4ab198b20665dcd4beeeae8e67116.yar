rule auto_rule_20250726065246_6049 {
  strings:
    $o0 = "x426860" wide ascii nocase
    $o1 = "off_462AEC" wide ascii nocase
    $o2 = "dword_4630F8" wide ascii nocase
  condition:
    3 of ($o*)
}