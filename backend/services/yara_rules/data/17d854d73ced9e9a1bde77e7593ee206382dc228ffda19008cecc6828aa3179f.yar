rule auto_rule_20250726095614_5129 {
  strings:
    $o0 = "init" wide ascii nocase
    $o1 = "dword_77F60" wide ascii nocase
  condition:
    all of them
}