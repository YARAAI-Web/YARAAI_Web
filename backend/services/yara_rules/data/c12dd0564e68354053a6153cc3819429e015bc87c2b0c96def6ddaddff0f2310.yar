rule auto_rule_20250727042243_4995 {
  strings:
    $o0 = "lpszStart" wide ascii nocase
    $o1 = "hwinsta" wide ascii nocase
    $o2 = "uCode" wide ascii nocase
    $o3 = "GetMenuBarInfo" wide ascii nocase
    $o4 = "GetSystemMenu" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727042247_6135 {
  strings:
    $o0 = "SetUserObjectInformationW" wide ascii nocase
    $o1 = "GetKBCodePage" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727042250_0006 {
  condition:
    auto_rule_20250727042243_4995 or auto_rule_20250727042247_6135
}