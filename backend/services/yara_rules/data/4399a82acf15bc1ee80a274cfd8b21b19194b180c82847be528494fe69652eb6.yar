rule auto_rule_20250726140828_1529 {
  strings:
    $o0 = "xA4Fu" wide ascii nocase
    $o1 = "dword_4292A2" wide ascii nocase
    $o2 = "dword_42A2C2" wide ascii nocase
  condition:
    3 of ($o*)
}