rule auto_rule_20250726115030_6504 {
  strings:
    $o0 = "dword_4283FB" wide ascii nocase
  condition:
    all of them
}