rule auto_rule_20250726085047_7222 {
  strings:
    $o0 = "dword_1400D1818" wide ascii nocase
    $o1 = "dword_1400D18D0" wide ascii nocase
    $o2 = "dword_1400D16B4" wide ascii nocase
    $o3 = "dword_1400D1958" wide ascii nocase
  condition:
    4 of ($o*)
}