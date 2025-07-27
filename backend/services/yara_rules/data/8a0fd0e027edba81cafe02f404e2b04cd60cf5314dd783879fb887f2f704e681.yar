rule auto_rule_20250726205453_3296 {
  strings:
    $o0 = "dword_44E1A0" wide ascii nocase
    $o1 = "fdwUnprepare" wide ascii nocase
    $o2 = "SchedulingNode" wide ascii nocase
  condition:
    3 of ($o*)
}