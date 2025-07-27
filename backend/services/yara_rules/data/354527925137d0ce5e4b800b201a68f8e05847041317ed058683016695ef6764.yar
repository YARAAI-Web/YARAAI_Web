rule auto_rule_20250726120135_8361 {
  strings:
    $o0 = "x8A29A147" wide ascii nocase
    $o1 = "dword_426ED5" wide ascii nocase
  condition:
    all of them
}