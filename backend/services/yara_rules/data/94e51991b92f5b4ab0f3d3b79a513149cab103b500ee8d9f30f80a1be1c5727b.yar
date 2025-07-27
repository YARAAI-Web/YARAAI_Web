rule auto_rule_20250726200513_9519 {
  strings:
    $o0 = "v362" wide ascii nocase
    $o1 = "dword_1400E1448" wide ascii nocase
  condition:
    all of them
}