rule auto_rule_20250727001833_3493 {
  strings:
    $o0 = "p_lpOptional" wide ascii nocase
    $o1 = "dword_1001EE60" wide ascii nocase
    $o2 = "Airrat" wide ascii nocase
  condition:
    3 of ($o*)
}