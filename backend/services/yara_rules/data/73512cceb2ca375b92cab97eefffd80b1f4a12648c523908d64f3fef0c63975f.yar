rule auto_rule_20250727021009_9735 {
  strings:
    $o0 = "dword_402F34" wide ascii nocase
    $o1 = "dword_42EED4" wide ascii nocase
    $o2 = "dword_42EED0" wide ascii nocase
  condition:
    3 of ($o*)
}