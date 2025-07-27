rule auto_rule_20250727003554_9498 {
  strings:
    $o0 = "x13A5" wide ascii nocase
    $o1 = "x1A3Fu" wide ascii nocase
    $o2 = "x4A4800000000LL" wide ascii nocase
  condition:
    3 of ($o*)
}