rule auto_rule_20250726173031_6859 {
  strings:
    $o0 = "dword_407700" wide ascii nocase
    $o1 = "dword_4072C0" wide ascii nocase
  condition:
    all of them
}