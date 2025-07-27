rule auto_rule_20250726193612_9978 {
  strings:
    $o0 = "dword_64031434" wide ascii nocase
    $o1 = "dword_64031450" wide ascii nocase
  condition:
    all of them
}