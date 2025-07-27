rule auto_rule_20250726215740_1422 {
  strings:
    $o0 = "SetPixel" wide ascii nocase
    $o1 = "x44ECu" wide ascii nocase
  condition:
    all of them
}