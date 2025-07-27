rule auto_rule_20250727014546_0308 {
  strings:
    $o0 = "x5572u" wide ascii nocase
    $o1 = "dword_42759C" wide ascii nocase
  condition:
    all of them
}