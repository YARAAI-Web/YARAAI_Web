rule auto_rule_20250726181730_2676 {
  strings:
    $o0 = "dword_77F60" wide ascii nocase
    $o1 = "dword_78118" wide ascii nocase
  condition:
    all of them
}