rule auto_rule_20250727014350_3643 {
  strings:
    $o0 = "word_40961C" wide ascii nocase
    $o1 = "TargetIp" wide ascii nocase
  condition:
    all of them
}