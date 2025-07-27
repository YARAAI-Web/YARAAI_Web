rule auto_rule_20250726110126_2102 {
  strings:
    $o0 = "dword_78160" wide ascii nocase
  condition:
    all of them
}