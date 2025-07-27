rule auto_rule_20250726222436_9415 {
  strings:
    $o0 = "VirtualAllocEx" wide ascii nocase
    $o1 = "lpIconName" wide ascii nocase
    $o2 = "dword_41D98C" wide ascii nocase
  condition:
    3 of ($o*)
}