rule auto_rule_20250727041102_5757 {
  strings:
    $o0 = "dword_47E014" wide ascii nocase
    $o1 = "dword_47EBB0" wide ascii nocase
    $o2 = "dword_47EE74" wide ascii nocase
  condition:
    3 of ($o*)
}