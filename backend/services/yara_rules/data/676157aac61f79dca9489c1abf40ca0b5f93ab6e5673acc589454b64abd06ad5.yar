rule auto_rule_20250727001615_9748 {
  strings:
    $o0 = "program" wide ascii nocase
    $o1 = "dword_463ADC" wide ascii nocase
    $o2 = "dword_464280" wide ascii nocase
  condition:
    3 of ($o*)
}