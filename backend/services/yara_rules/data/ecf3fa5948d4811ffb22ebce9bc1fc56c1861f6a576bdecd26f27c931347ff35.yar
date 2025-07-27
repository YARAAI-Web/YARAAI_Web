rule auto_rule_20250726095638_9433 {
  strings:
    $o0 = "dword_40E2E4" wide ascii nocase
  condition:
    all of them
}