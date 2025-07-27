rule auto_rule_20250726193103_5641 {
  strings:
    $o0 = "FatTime" wide ascii nocase
    $o1 = "hDesktop" wide ascii nocase
    $o2 = "EnumWindowStationsW" wide ascii nocase
    $o3 = "uIDEnableItem" wide ascii nocase
    $o4 = "hsz1" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726193107_6522 {
  strings:
    $o0 = "ptszClassName" wide ascii nocase
    $o1 = "RemovePropW" wide ascii nocase
    $o2 = "uiAction" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726193111_3853 {
  condition:
    auto_rule_20250726193103_5641 or auto_rule_20250726193107_6522
}