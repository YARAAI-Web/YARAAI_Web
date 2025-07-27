rule auto_rule_20250726224251_8143 {
  strings:
    $o0 = "_NLG_Notify" wide ascii nocase
    $o1 = "off_4494C0" wide ascii nocase
    $o2 = "memcpy_0" wide ascii nocase
    $o3 = "_heap_alloc" wide ascii nocase
    $o4 = "dword_407004" wide ascii nocase
  condition:
    4 of ($o*)
}