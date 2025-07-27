rule auto_rule_20250726114546_5262 {
  strings:
    $o0 = "dword_4C1314" wide ascii nocase
  condition:
    all of them
}