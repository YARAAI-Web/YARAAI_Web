rule auto_rule_20250726152059_3321 {
  strings:
    $o0 = "ImpersonateDdeClientWindow" wide ascii nocase
    $o1 = "Process32Next" wide ascii nocase
  condition:
    all of them
}