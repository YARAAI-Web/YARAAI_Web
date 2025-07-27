rule auto_rule_20250726155330_6936 {
  strings:
    $o0 = "x797300000018LL" wide ascii nocase
  condition:
    all of them
}