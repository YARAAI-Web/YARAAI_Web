rule auto_rule_20250726113256_3110 {
  strings:
    $o0 = "dword_45D180" wide ascii nocase
    $o1 = "byte_45D080" wide ascii nocase
    $o2 = "_NLG_Notify" wide ascii nocase
    $o3 = "__sbh_alloc_block" wide ascii nocase
  condition:
    4 of ($o*)
}