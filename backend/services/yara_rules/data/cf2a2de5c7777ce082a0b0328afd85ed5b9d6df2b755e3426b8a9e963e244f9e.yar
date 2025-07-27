rule auto_rule_20250726205832_6313 {
  strings:
    $o0 = "lstrcatA" wide ascii nocase
    $o1 = "x17000u" wide ascii nocase
    $o2 = "flAllocationType" wide ascii nocase
  condition:
    3 of ($o*)
}