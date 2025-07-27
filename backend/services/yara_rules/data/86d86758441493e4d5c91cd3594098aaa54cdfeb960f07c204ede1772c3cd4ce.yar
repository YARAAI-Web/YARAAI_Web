rule auto_rule_20250726170201_5592 {
  strings:
    $o0 = "_abnormal_termination" wide ascii nocase
    $o1 = "dword_44C6D4" wide ascii nocase
    $o2 = "fill_dwords_with_EOS" wide ascii nocase
  condition:
    3 of ($o*)
}