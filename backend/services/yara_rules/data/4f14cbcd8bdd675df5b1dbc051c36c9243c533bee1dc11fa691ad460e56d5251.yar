rule auto_rule_20250726121543_5224 {
  strings:
    $o0 = "dword_40E538" wide ascii nocase
    $o1 = "dword_40ED50" wide ascii nocase
  condition:
    all of them
}