rule auto_rule_20250726065256_5464 {
  strings:
    $o0 = "aProgid" wide ascii nocase
    $o1 = "dword_4183B8" wide ascii nocase
  condition:
    all of them
}