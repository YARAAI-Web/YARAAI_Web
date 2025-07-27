rule auto_rule_20250726183524_8745 {
  strings:
    $o0 = "dword_42A3CA" wide ascii nocase
  condition:
    all of them
}