rule auto_rule_20250727020815_7861 {
  strings:
    $o0 = "dword_4279A0" wide ascii nocase
  condition:
    all of them
}