rule auto_rule_20250726210315_8869 {
  strings:
    $o0 = "SystemRoutineName" wide ascii nocase
    $o1 = "dword_78184" wide ascii nocase
  condition:
    all of them
}