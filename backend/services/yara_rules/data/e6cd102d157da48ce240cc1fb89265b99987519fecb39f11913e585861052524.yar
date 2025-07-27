rule auto_rule_20250726065756_2851 {
  strings:
    $o0 = "dword_4D30B4" wide ascii nocase
  condition:
    all of them
}