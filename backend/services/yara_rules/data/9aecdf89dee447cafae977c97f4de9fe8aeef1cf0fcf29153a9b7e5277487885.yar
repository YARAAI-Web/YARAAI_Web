rule auto_rule_20250727044159_3654 {
  strings:
    $o0 = "dword_427984" wide ascii nocase
    $o1 = "lstrcatW" wide ascii nocase
    $o2 = "dword_402F38" wide ascii nocase
  condition:
    3 of ($o*)
}