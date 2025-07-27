rule auto_rule_20250726182802_8835 {
  strings:
    $o0 = "dword_428643" wide ascii nocase
    $o1 = "dword_42860B" wide ascii nocase
    $o2 = "off_42830F" wide ascii nocase
  condition:
    3 of ($o*)
}