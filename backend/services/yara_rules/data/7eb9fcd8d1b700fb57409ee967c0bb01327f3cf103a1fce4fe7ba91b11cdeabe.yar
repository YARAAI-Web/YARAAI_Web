rule auto_rule_20250726061509_1489 {
  strings:
    $o0 = "dword_411AE8" wide ascii nocase
    $o1 = "TargetIp" wide ascii nocase
    $o2 = "dword_40E014" wide ascii nocase
    $o3 = "dword_411974" wide ascii nocase
    $o4 = "_cinit" wide ascii nocase
  condition:
    4 of ($o*)
}