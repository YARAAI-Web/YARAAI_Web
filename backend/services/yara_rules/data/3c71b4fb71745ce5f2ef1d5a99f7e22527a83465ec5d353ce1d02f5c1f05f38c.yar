rule auto_rule_20250726140352_4399 {
  strings:
    $o0 = "dword_10097980" wide ascii nocase
  condition:
    all of them
}