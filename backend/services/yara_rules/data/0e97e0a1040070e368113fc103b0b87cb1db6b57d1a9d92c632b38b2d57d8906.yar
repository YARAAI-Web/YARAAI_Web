rule auto_rule_20250726143325_2688 {
  strings:
    $o0 = "dword_78160" wide ascii nocase
    $o1 = "dword_78374" wide ascii nocase
    $o2 = "init" wide ascii nocase
  condition:
    3 of ($o*)
}