rule auto_rule_20250726212035_8322 {
  strings:
    $o0 = "lpszNewItem" wide ascii nocase
    $o1 = "IMPSetIMEA" wide ascii nocase
    $o2 = "UnpackDDElParam" wide ascii nocase
    $o3 = "nIDStaticPath" wide ascii nocase
    $o4 = "GetAsyncKeyState" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726212038_1686 {
  strings:
    $o0 = "MapVirtualKeyExA" wide ascii nocase
    $o1 = "lpClipRect" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726212042_2200 {
  condition:
    auto_rule_20250726212035_8322 or auto_rule_20250726212038_1686
}