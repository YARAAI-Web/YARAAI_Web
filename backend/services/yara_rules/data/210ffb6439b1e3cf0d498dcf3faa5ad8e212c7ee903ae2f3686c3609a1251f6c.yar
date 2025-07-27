rule auto_rule_20250727035926_0849 {
  strings:
    $o0 = "nTabPositions" wide ascii nocase
    $o1 = "x3EFD00003993LL" wide ascii nocase
  condition:
    all of them
}