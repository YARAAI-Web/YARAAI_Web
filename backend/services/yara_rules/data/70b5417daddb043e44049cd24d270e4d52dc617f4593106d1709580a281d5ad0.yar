rule auto_rule_20250726070346_0452 {
  strings:
    $o0 = "dword_469080" wide ascii nocase
    $o1 = "byte_4691C0" wide ascii nocase
    $o2 = "xC0000093" wide ascii nocase
    $o3 = "__sbh_alloc_block" wide ascii nocase
  condition:
    4 of ($o*)
}