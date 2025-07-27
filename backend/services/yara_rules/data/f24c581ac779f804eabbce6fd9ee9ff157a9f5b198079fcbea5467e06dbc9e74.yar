rule auto_rule_20250727000349_1605 {
  strings:
    $o0 = "hInstApp" wide ascii nocase
    $o1 = "dword_42BA40" wide ascii nocase
  condition:
    all of them
}