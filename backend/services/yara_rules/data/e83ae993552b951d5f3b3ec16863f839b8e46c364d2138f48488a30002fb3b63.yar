rule auto_rule_20250726131413_2329 {
  strings:
    $o0 = "off_479024" wide ascii nocase
    $o1 = "x412CC5" wide ascii nocase
  condition:
    all of them
}