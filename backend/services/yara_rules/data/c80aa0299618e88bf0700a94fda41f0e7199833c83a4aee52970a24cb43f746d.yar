rule auto_rule_20250726120839_3365 {
  strings:
    $o0 = "VirtualFree" wide ascii nocase
    $o1 = "fill_dwords_with_EOS" wide ascii nocase
    $o2 = "byte_46ED60" wide ascii nocase
  condition:
    3 of ($o*)
}