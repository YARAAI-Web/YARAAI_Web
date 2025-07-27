rule auto_rule_20250726061624_8669 {
  strings:
    $o0 = "dword_782F8" wide ascii nocase
    $o1 = "dword_78160" wide ascii nocase
  condition:
    all of them
}