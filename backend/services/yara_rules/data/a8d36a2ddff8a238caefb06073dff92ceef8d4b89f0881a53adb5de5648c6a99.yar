rule auto_rule_20250726184758_9827 {
  strings:
    $o0 = "KeReleaseMutex" wide ascii nocase
    $o1 = "KeGetCurrentIrql" wide ascii nocase
    $o2 = "dword_78338" wide ascii nocase
  condition:
    3 of ($o*)
}