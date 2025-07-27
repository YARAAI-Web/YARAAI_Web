rule auto_rule_20250726201103_6366 {
  strings:
    $o0 = "dword_4AE054" wide ascii nocase
    $o1 = "dword_4B4BA4" wide ascii nocase
  condition:
    all of them
}