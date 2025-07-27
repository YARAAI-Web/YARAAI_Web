rule auto_rule_20250726171232_3773 {
  strings:
    $o0 = "dword_42D000" wide ascii nocase
    $o1 = "x643Fu" wide ascii nocase
    $o2 = "dword_429010" wide ascii nocase
  condition:
    3 of ($o*)
}