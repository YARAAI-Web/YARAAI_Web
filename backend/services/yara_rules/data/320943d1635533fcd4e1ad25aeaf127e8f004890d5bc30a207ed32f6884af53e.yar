rule auto_rule_20250726105643_1208 {
  strings:
    $o0 = "AssocQueryStringA" wide ascii nocase
    $o1 = "nIDComboBox" wide ascii nocase
    $o2 = "GetIconInfo" wide ascii nocase
    $o3 = "cKids" wide ascii nocase
    $o4 = "hwinsta" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726105646_2053 {
  strings:
    $o0 = "StrPBrkW" wide ascii nocase
    $o1 = "PathUndecorateW" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726105650_8348 {
  condition:
    auto_rule_20250726105643_1208 or auto_rule_20250726105646_2053
}