rule auto_rule_20250726150124_4525 {
  strings:
    $o0 = "lpSecurityAttributes" wide ascii nocase
    $o1 = "dwCreationDisposition" wide ascii nocase
    $o2 = "dword_402F38" wide ascii nocase
  condition:
    3 of ($o*)
}