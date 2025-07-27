rule auto_rule_20250726103148_4150 {
  strings:
    $o0 = "dword_42EED8" wide ascii nocase
    $o1 = "dword_42EEB0" wide ascii nocase
    $o2 = "dword_402F34" wide ascii nocase
    $o3 = "dword_42EEB4" wide ascii nocase
  condition:
    4 of ($o*)
}