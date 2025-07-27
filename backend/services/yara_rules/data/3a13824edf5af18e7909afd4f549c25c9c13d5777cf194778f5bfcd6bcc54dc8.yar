rule auto_rule_20250727000552_7553 {
  strings:
    $o0 = "CreateMDIWindowW" wide ascii nocase
    $o1 = "pptDst" wide ascii nocase
    $o2 = "lpEnumFunc" wide ascii nocase
    $o3 = "DrawFocusRect" wide ascii nocase
    $o4 = "EnumDesktopsA" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727000555_2219 {
  strings:
    $o0 = "DdeReconnect" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727000559_4065 {
  condition:
    auto_rule_20250727000552_7553 or auto_rule_20250727000555_2219
}