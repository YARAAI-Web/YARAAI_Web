rule auto_rule_20250727003322_0709 {
  strings:
    $o0 = "dword_6402FD90" wide ascii nocase
  condition:
    all of them
}