rule auto_rule_20250727044759_2925 {
  strings:
    $o0 = "dword_7820C" wide ascii nocase
    $o1 = "dword_78194" wide ascii nocase
  condition:
    all of them
}