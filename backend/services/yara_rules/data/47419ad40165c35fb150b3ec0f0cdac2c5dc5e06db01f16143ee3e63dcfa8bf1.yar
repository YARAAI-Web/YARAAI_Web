rule auto_rule_20250726160511_4612 {
  strings:
    $o0 = "fccHandler" wide ascii nocase
  condition:
    all of them
}