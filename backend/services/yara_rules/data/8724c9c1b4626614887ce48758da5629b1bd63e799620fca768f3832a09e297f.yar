rule auto_rule_20250726112301_5456 {
  strings:
    $o0 = "x4F4u" wide ascii nocase
    $o1 = "PeekMessagePeekMessageA" wide ascii nocase
  condition:
    all of them
}