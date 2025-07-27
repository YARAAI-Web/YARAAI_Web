rule auto_rule_20250727024210_2378 {
  strings:
    $o0 = "x5164" wide ascii nocase
  condition:
    all of them
}