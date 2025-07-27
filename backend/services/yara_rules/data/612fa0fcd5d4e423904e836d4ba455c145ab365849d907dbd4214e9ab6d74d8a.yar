rule auto_rule_20250727014808_3489 {
  strings:
    $o0 = "x87B3" wide ascii nocase
    $o1 = "AreFileApisANSI" wide ascii nocase
    $o2 = "x634E" wide ascii nocase
    $o3 = "x620Fu" wide ascii nocase
  condition:
    4 of ($o*)
}