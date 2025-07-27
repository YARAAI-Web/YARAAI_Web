rule auto_rule_20250726101348_0872 {
  strings:
    $o0 = "grfMode" wide ascii nocase
    $o1 = "SHRegDeleteEmptyUSKeyW" wide ascii nocase
    $o2 = "bScan" wide ascii nocase
    $o3 = "IsCharLowerA" wide ascii nocase
    $o4 = "CloseWindow" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726101351_6495 {
  strings:
    $o0 = "pcchUrl" wide ascii nocase
    $o1 = "uIDNewItem" wide ascii nocase
    $o2 = "pszUnescaped" wide ascii nocase
    $o3 = "GetMenuBarInfo" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726101356_5155 {
  condition:
    auto_rule_20250726101348_0872 or auto_rule_20250726101351_6495
}