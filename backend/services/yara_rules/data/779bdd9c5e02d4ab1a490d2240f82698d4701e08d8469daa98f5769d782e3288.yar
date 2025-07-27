rule auto_rule_20250726112503_7487 {
  strings:
    $o0 = "dword_42EEAC" wide ascii nocase
  condition:
    all of them
}