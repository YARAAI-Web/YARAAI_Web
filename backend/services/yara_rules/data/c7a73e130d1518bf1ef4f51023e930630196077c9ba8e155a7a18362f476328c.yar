rule auto_rule_20250726201239_8051 {
  strings:
    $o0 = "cchItemText" wide ascii nocase
    $o1 = "cchMaxCount" wide ascii nocase
    $o2 = "hWndRemove" wide ascii nocase
    $o3 = "EnumPropsA" wide ascii nocase
    $o4 = "hRecipient" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726201242_7763 {
  strings:
    $o0 = "iItem" wide ascii nocase
    $o1 = "SetWindowsHookW" wide ascii nocase
    $o2 = "pvInfo" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726201246_4915 {
  condition:
    auto_rule_20250726201239_8051 or auto_rule_20250726201242_7763
}