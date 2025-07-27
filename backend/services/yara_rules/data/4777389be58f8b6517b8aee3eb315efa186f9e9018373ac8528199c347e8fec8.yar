rule auto_rule_20250726210903_4660 {
  strings:
    $o0 = "dword_41D97C" wide ascii nocase
  condition:
    all of them
}