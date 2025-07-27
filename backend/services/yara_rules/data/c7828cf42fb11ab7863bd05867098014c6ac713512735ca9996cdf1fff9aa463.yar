rule auto_rule_20250726115221_5890 {
  strings:
    $o0 = "bPrevious" wide ascii nocase
    $o1 = "GetGuiResources" wide ascii nocase
    $o2 = "uCode" wide ascii nocase
    $o3 = "DdeCreateStringHandleA" wide ascii nocase
    $o4 = "nBar" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726115223_3871 {
  strings:
    $o0 = "ulOptions" wide ascii nocase
    $o1 = "dwLevel" wide ascii nocase
    $o2 = "GetCaretBlinkTime" wide ascii nocase
    $o3 = "x17000u" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726115226_5573 {
  condition:
    auto_rule_20250726115221_5890 or auto_rule_20250726115223_3871
}