rule auto_rule_20250726155543_0449 {
  strings:
    $o0 = "dword_45D268" wide ascii nocase
  condition:
    all of them
}