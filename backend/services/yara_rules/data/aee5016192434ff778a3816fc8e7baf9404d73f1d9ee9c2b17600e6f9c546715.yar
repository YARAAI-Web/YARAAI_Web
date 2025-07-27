rule auto_rule_20250726152228_5514 {
  strings:
    $o0 = "off_456490" wide ascii nocase
    $o1 = "Runtime" wide ascii nocase
    $o2 = "CopyUnwindUp_0" wide ascii nocase
  condition:
    3 of ($o*)
}