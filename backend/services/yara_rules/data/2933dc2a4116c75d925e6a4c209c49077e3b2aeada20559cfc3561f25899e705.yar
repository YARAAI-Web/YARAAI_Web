rule auto_rule_20250726175000_0761 {
  strings:
    $o0 = "x3F000u" wide ascii nocase
    $o1 = "aClsid" wide ascii nocase
  condition:
    all of them
}