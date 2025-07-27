rule auto_rule_20250727013835_2243 {
  strings:
    $o0 = "dword_4C1340" wide ascii nocase
  condition:
    all of them
}