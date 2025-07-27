rule auto_rule_20250726114409_5411 {
  strings:
    $o0 = "x436BDF38" wide ascii nocase
  condition:
    all of them
}