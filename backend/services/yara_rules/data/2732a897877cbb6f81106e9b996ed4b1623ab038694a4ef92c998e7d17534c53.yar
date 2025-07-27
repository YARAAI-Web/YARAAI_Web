rule auto_rule_20250726140439_5345 {
  strings:
    $o0 = "dword_45D440" wide ascii nocase
    $o1 = "algn_45E032" wide ascii nocase
  condition:
    all of them
}