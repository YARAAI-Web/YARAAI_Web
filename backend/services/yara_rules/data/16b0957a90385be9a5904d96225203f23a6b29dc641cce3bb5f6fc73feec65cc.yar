rule auto_rule_20250726093450_9946 {
  strings:
    $o0 = "dword_44A3B8" wide ascii nocase
    $o1 = "Runtime" wide ascii nocase
    $o2 = "CodePagea" wide ascii nocase
  condition:
    3 of ($o*)
}