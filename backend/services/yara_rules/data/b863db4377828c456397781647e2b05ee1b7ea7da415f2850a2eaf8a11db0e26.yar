rule auto_rule_20250726085840_5881 {
  strings:
    $o0 = "dword_1400DB8A8" wide ascii nocase
    $o1 = "dword_1400DB6BC" wide ascii nocase
    $o2 = "dword_1400DB428" wide ascii nocase
  condition:
    3 of ($o*)
}