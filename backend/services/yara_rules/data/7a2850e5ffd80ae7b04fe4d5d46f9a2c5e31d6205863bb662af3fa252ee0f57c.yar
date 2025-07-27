rule auto_rule_20250726185051_4269 {
  strings:
    $o0 = "x8A29A127" wide ascii nocase
  condition:
    all of them
}