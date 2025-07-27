rule auto_rule_20250726201530_8621 {
  strings:
    $o0 = "dword_401220" wide ascii nocase
    $o1 = "dword_41B000" wide ascii nocase
  condition:
    all of them
}