rule auto_rule_20250726132710_8300 {
  strings:
    $o0 = "_NLG_Notify1" wide ascii nocase
    $o1 = "dword_45C2D4" wide ascii nocase
    $o2 = "TrailUp3" wide ascii nocase
    $o3 = "_NLG_Notify" wide ascii nocase
    $o4 = "dwInfoType" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726132713_6853 {
  strings:
    $o0 = "dword_45C440" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726132723_9295 {
  condition:
    auto_rule_20250726132710_8300 or auto_rule_20250726132713_6853
}