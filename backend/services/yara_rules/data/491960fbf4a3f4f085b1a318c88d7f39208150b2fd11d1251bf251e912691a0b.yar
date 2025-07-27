rule auto_rule_20250726184041_7239 {
  strings:
    $o0 = "CreatePipe" wide ascii nocase
    $o1 = "Denied" wide ascii nocase
    $o2 = "NtFreeVirtualMemory" wide ascii nocase
  condition:
    3 of ($o*)
}