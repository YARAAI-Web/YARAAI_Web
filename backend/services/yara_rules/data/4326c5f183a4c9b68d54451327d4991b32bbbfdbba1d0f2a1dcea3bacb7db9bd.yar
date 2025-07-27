rule auto_rule_20250726201314_2253 {
  strings:
    $o0 = "dword_78334" wide ascii nocase
    $o1 = "dword_78450" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}