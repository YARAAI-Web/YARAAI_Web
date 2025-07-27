rule auto_rule_20250726112840_5231 {
  strings:
    $o0 = "PeekMessagePeekMessageA" wide ascii nocase
    $o1 = "x8A99" wide ascii nocase
    $o2 = "off_42830B" wide ascii nocase
  condition:
    3 of ($o*)
}