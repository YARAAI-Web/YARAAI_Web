rule auto_rule_20250726222445_0644 {
  strings:
    $o0 = "dword_45D8AC" wide ascii nocase
  condition:
    all of them
}