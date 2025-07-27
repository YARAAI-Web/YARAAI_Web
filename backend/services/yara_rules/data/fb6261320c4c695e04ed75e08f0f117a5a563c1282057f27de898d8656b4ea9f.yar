rule auto_rule_20250726101555_3533 {
  strings:
    $o0 = "dword_780F8" wide ascii nocase
    $o1 = "ExAllocatePoolWithTagPriority" wide ascii nocase
  condition:
    all of them
}