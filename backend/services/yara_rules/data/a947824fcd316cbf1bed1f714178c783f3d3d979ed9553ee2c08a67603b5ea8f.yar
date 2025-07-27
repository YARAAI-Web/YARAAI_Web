rule auto_rule_20250726090303_6532 {
  strings:
    $o0 = "x4B6B" wide ascii nocase
    $o1 = "x39F6" wide ascii nocase
    $o2 = "xE149EBEu" wide ascii nocase
  condition:
    3 of ($o*)
}