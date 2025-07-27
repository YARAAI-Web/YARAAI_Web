rule auto_rule_20250726152752_7204 {
  strings:
    $o0 = "dword_455A0C" wide ascii nocase
    $o1 = "dword_454F0C" wide ascii nocase
  condition:
    all of them
}