rule auto_rule_20250726155018_2738 {
  strings:
    $o0 = "dword_44E1AC" wide ascii nocase
  condition:
    all of them
}