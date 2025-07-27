rule auto_rule_20250727035257_5569 {
  strings:
    $o0 = "dword_4281E8" wide ascii nocase
    $o1 = "dword_4280A8" wide ascii nocase
    $o2 = "byte_427688" wide ascii nocase
    $o3 = "_cftoe_g" wide ascii nocase
    $o4 = "_heap_alloc" wide ascii nocase
  condition:
    4 of ($o*)
}