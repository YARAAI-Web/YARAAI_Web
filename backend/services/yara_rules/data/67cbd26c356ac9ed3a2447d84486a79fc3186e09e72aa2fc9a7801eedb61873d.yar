rule auto_rule_20250726065352_3878 {
  strings:
    $o0 = "EnumDisplaySettingsExA" wide ascii nocase
    $o1 = "crKey" wide ascii nocase
    $o2 = "hData" wide ascii nocase
    $o3 = "PaintDesktop" wide ascii nocase
    $o4 = "pdwDefaultLayout" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726065355_2662 {
  strings:
    $o0 = "uFiletype" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726065400_6873 {
  condition:
    auto_rule_20250726065352_3878 or auto_rule_20250726065355_2662
}