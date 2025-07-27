rule auto_rule_20250726151907_3511 {
  strings:
    $o0 = "dword_411974" wide ascii nocase
    $o1 = "dword_411D40" wide ascii nocase
    $o2 = "fill_dwords_with_EOS" wide ascii nocase
    $o3 = "start_byte_3" wide ascii nocase
  condition:
    4 of ($o*)
}