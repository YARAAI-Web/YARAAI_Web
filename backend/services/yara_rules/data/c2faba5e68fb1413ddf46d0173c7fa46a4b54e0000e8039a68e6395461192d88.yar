rule auto_rule_20250726194753_4111 {
  strings:
    $o0 = "dword_42EEBC" wide ascii nocase
    $o1 = "dwFlagsAndAttributes" wide ascii nocase
  condition:
    all of them
}