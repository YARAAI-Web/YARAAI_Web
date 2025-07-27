rule auto_rule_20250726084755_5994 {
  strings:
    $o0 = "m128i_u32" wide ascii nocase
    $o1 = "xFFFFFFFFFFFFFFE0uLL" wide ascii nocase
    $o2 = "byte_1400200E0" wide ascii nocase
    $o3 = "recalloc_base" wide ascii nocase
    $o4 = "rdata" wide ascii nocase
  condition:
    5 of ($o*)
}