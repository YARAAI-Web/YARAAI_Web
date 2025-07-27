rule auto_rule_20250726162826_6704 {
  strings:
    $o0 = "dword_4577AC" wide ascii nocase
  condition:
    all of them
}