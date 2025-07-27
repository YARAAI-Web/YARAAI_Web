rule auto_rule_20250726214158_6332 {
  strings:
    $o0 = "dword_44BE78" wide ascii nocase
  condition:
    all of them
}