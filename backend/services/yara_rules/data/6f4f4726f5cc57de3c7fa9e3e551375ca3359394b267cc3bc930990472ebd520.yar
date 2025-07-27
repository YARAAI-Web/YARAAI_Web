rule auto_rule_20250726162021_1016 {
  strings:
    $o0 = "dword_6402F190" wide ascii nocase
    $o1 = "Services" wide ascii nocase
  condition:
    all of them
}