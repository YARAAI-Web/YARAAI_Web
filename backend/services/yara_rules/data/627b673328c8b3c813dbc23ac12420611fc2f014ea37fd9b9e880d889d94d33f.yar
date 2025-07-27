rule auto_rule_20250726192009_5570 {
  strings:
    $o0 = "dword_446ECC" wide ascii nocase
  condition:
    all of them
}