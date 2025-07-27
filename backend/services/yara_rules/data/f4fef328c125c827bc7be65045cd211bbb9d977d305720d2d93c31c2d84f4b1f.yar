rule auto_rule_20250726220245_4375 {
  strings:
    $o0 = "cause" wide ascii nocase
    $o1 = "terminated" wide ascii nocase
    $o2 = "dword_476AC8" wide ascii nocase
  condition:
    3 of ($o*)
}