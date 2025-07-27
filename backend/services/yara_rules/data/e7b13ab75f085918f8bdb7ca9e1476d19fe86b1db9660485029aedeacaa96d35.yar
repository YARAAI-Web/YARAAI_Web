rule auto_rule_20250726064754_3269 {
  strings:
    $o0 = "dword_456930" wide ascii nocase
    $o1 = "dword_4570CC" wide ascii nocase
  condition:
    all of them
}