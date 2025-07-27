rule auto_rule_20250727033844_4635 {
  strings:
    $o0 = "dword_40CE30" wide ascii nocase
    $o1 = "dword_40CFD8" wide ascii nocase
    $o2 = "dword_40CFA0" wide ascii nocase
    $o3 = "dword_40CE28" wide ascii nocase
  condition:
    4 of ($o*)
}