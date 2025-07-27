rule auto_rule_20250726193052_4799 {
  strings:
    $o0 = "type__eq_internal_abi_UncommonType" wide ascii nocase
    $o1 = "internal_stringslite_Index" wide ascii nocase
  condition:
    all of them
}