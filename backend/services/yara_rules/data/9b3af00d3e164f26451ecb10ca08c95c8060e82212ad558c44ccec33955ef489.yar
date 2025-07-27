rule auto_rule_20250726061602_1827 {
  strings:
    $o0 = "dword_46D1B4" wide ascii nocase
    $o1 = "LibraryA" wide ascii nocase
  condition:
    all of them
}