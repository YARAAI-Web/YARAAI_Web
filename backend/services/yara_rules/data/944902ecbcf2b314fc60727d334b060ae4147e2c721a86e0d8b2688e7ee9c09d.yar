rule auto_rule_20250726103328_7204 {
  strings:
    $o0 = "dword_775B4" wide ascii nocase
    $o1 = "init" wide ascii nocase
  condition:
    all of them
}