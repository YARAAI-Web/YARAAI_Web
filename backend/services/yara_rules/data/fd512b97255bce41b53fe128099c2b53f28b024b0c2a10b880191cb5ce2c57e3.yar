rule auto_rule_20250726163234_2443 {
  strings:
    $o0 = "dword_1400C7574" wide ascii nocase
    $o1 = "dword_1400C7544" wide ascii nocase
    $o2 = "v336" wide ascii nocase
  condition:
    3 of ($o*)
}