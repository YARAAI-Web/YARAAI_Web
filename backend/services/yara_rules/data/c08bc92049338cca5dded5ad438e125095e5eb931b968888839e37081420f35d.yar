rule auto_rule_20250726193348_5167 {
  strings:
    $o0 = "dword_1400D18BC" wide ascii nocase
    $o1 = "dword_1400D1A40" wide ascii nocase
    $o2 = "dword_1400D1998" wide ascii nocase
  condition:
    3 of ($o*)
}