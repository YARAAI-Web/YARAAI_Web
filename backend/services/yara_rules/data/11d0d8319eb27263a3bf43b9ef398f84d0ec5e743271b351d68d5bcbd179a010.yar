rule auto_rule_20250727043327_2260 {
  strings:
    $o0 = "dword_4030BC" wide ascii nocase
    $o1 = "x960u" wide ascii nocase
    $o2 = "dword_402F34" wide ascii nocase
  condition:
    3 of ($o*)
}