rule auto_rule_20250726133448_9780 {
  strings:
    $o0 = "aProgid" wide ascii nocase
    $o1 = "dword_4182EC" wide ascii nocase
  condition:
    all of them
}