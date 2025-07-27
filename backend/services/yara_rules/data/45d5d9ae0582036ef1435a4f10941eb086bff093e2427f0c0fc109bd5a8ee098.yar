rule auto_rule_20250726130008_0878 {
  strings:
    $o0 = "dword_4040FC" wide ascii nocase
    $o1 = "dword_4041F8" wide ascii nocase
    $o2 = "dword_4040B0" wide ascii nocase
  condition:
    3 of ($o*)
}