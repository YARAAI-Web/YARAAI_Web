rule auto_rule_20250727005656_4544 {
  strings:
    $o0 = "uCmd" wide ascii nocase
    $o1 = "iItem" wide ascii nocase
    $o2 = "CallMsgFilter" wide ascii nocase
    $o3 = "uEnable" wide ascii nocase
    $o4 = "ChangeDisplaySettingsExW" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727005659_9498 {
  strings:
    $o0 = "TileChildWindows" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727005701_5753 {
  condition:
    auto_rule_20250727005656_4544 or auto_rule_20250727005659_9498
}