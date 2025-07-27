rule auto_rule_20250727011334_5855 {
  strings:
    $o0 = "dword_78308" wide ascii nocase
    $o1 = "ExAllocatePoolWithTag" wide ascii nocase
  condition:
    all of them
}