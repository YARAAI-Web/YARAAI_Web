rule auto_rule_20250726221956_2947 {
  strings:
    $o0 = "TrailUp0_0" wide ascii nocase
    $o1 = "dword_45D3F0" wide ascii nocase
    $o2 = "Handler" wide ascii nocase
    $o3 = "fill_dwords_with_EOS" wide ascii nocase
    $o4 = "_heap_alloc" wide ascii nocase
  condition:
    5 of ($o*)
}