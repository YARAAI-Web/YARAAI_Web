rule auto_rule_20250726150702_8921 {
  strings:
    $o0 = "_cfltcvt" wide ascii nocase
    $o1 = "atol" wide ascii nocase
    $o2 = "off_456B74" wide ascii nocase
  condition:
    3 of ($o*)
}