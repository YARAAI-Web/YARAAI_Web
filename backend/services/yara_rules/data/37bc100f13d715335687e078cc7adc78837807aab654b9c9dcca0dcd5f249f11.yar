rule auto_rule_20250726091352_0982 {
  strings:
    $o0 = "dword_64030364" wide ascii nocase
  condition:
    all of them
}