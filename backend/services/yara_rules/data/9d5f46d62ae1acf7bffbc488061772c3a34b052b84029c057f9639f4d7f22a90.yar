rule auto_rule_20250727024710_0095 {
  strings:
    $o0 = "lpTimerName" wide ascii nocase
    $o1 = "yBottom" wide ascii nocase
  condition:
    all of them
}