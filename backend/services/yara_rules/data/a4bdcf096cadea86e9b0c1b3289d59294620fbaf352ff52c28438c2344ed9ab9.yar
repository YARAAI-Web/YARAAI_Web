rule auto_rule_20250726232415_6897 {
  strings:
    $o0 = "dword_476E20" wide ascii nocase
  condition:
    all of them
}