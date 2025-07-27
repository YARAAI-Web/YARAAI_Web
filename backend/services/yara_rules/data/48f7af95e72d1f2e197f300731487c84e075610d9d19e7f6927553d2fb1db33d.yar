rule auto_rule_20250727003701_9675 {
  strings:
    $o0 = "dword_437763" wide ascii nocase
  condition:
    all of them
}