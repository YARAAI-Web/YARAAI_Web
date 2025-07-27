rule auto_rule_20250726232332_3129 {
  strings:
    $o0 = "off_42415A" wide ascii nocase
    $o1 = "dword_42B004" wide ascii nocase
  condition:
    all of them
}