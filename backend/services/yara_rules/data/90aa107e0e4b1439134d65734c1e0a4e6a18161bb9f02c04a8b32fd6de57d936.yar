rule auto_rule_20250727014511_1273 {
  strings:
    $o0 = "EnumResourceNamesW" wide ascii nocase
    $o1 = "lpDCB" wide ascii nocase
    $o2 = "lpCommProp" wide ascii nocase
    $o3 = "OpenFileMappingW" wide ascii nocase
    $o4 = "nAtom" wide ascii nocase
  condition:
    4 of ($o*)
}