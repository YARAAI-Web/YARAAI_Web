rule auto_rule_20250726213624_3258 {
  strings:
    $o0 = "_wwincmdln" wide ascii nocase
    $o1 = "_forcdecpt" wide ascii nocase
    $o2 = "dword_4C02D8" wide ascii nocase
    $o3 = "dword_48D88C" wide ascii nocase
    $o4 = "_Error_handling_1" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726213628_8202 {
  strings:
    $o0 = "dword_4B6A24" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726213632_9064 {
  condition:
    auto_rule_20250726213624_3258 or auto_rule_20250726213628_8202
}