rule auto_rule_20250726085952_0349 {
  strings:
    $o0 = "StrStrIA" wide ascii nocase
    $o1 = "GetAltTabInfoW" wide ascii nocase
    $o2 = "MsgWaitForMultipleObjectsEx" wide ascii nocase
    $o3 = "StrRChrW" wide ascii nocase
    $o4 = "GetAsyncKeyState" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726085955_0828 {
  strings:
    $o0 = "PathFindOnPathA" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726085958_2664 {
  condition:
    auto_rule_20250726085952_0349 or auto_rule_20250726085955_0828
}