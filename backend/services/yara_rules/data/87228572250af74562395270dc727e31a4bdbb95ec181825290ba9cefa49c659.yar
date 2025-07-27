rule auto_rule_20250726093501_8693 {
  strings:
    $o0 = "dword_411984" wide ascii nocase
    $o1 = "dword_40E014" wide ascii nocase
    $o2 = "strcat" wide ascii nocase
  condition:
    3 of ($o*)
}