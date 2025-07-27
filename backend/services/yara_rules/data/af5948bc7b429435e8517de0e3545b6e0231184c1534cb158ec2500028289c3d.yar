rule auto_rule_20250726224031_2719 {
  strings:
    $o0 = "dword_467304" wide ascii nocase
    $o1 = "Client" wide ascii nocase
    $o2 = "uChar" wide ascii nocase
  condition:
    3 of ($o*)
}