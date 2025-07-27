rule auto_rule_20250726132654_6237 {
  strings:
    $o0 = "GetKeyNameTextA" wide ascii nocase
    $o1 = "lpBitmapName" wide ascii nocase
    $o2 = "hObj" wide ascii nocase
    $o3 = "nIDFirstButton" wide ascii nocase
    $o4 = "lpszCurrent" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726132657_2777 {
  strings:
    $o0 = "GetUserObjectSecurity" wide ascii nocase
    $o1 = "WINNLSEnableIME" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726132701_3946 {
  condition:
    auto_rule_20250726132654_6237 or auto_rule_20250726132657_2777
}