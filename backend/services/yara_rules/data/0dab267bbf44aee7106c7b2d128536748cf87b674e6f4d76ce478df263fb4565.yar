rule auto_rule_20250726223012_6382 {
  strings:
    $o0 = "dodwords" wide ascii nocase
    $o1 = "x415640" wide ascii nocase
    $o2 = "off_44BF88" wide ascii nocase
    $o3 = "UnwindUp2_0" wide ascii nocase
  condition:
    4 of ($o*)
}