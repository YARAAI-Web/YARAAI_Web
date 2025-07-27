rule auto_rule_20250726075802_9453 {
  strings:
    $o0 = "dword_4617B0" wide ascii nocase
    $o1 = "Offset" wide ascii nocase
    $o2 = "dword_4605FC" wide ascii nocase
  condition:
    3 of ($o*)
}