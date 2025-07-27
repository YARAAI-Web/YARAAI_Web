rule auto_rule_20250726102427_2317 {
  strings:
    $o0 = "dword_4C1294" wide ascii nocase
  condition:
    all of them
}