rule auto_rule_20250726171854_6642 {
  strings:
    $o0 = "PsLookupProcessByProcessId" wide ascii nocase
    $o1 = "PoolWithTagPriority" wide ascii nocase
    $o2 = "dword_78354" wide ascii nocase
  condition:
    3 of ($o*)
}