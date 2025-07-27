rule auto_rule_20250726180227_1744 {
  strings:
    $o0 = "dword_42B014" wide ascii nocase
    $o1 = "x848Fu" wide ascii nocase
  condition:
    all of them
}