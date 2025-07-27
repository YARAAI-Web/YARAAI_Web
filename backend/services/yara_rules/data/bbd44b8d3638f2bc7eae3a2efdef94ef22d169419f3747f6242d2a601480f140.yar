rule auto_rule_20250727000013_2923 {
  strings:
    $o0 = "dword_40E000" wide ascii nocase
    $o1 = "dword_411590" wide ascii nocase
  condition:
    all of them
}