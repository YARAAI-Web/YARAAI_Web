rule auto_rule_20250727042715_8248 {
  strings:
    $o0 = "RegisterShellHookWindow" wide ascii nocase
    $o1 = "EnumPropsA" wide ascii nocase
    $o2 = "cchText" wide ascii nocase
    $o3 = "uiAction" wide ascii nocase
    $o4 = "LoadKeyboardLayoutA" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727042718_0523 {
  strings:
    $o0 = "idObject" wide ascii nocase
    $o1 = "wScanCode" wide ascii nocase
    $o2 = "DefMDIChildProcA" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250727042724_4978 {
  condition:
    auto_rule_20250727042715_8248 or auto_rule_20250727042718_0523
}