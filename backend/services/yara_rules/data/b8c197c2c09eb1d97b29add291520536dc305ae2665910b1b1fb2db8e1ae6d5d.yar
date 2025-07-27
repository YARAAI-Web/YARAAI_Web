rule auto_rule_20250726140318_2194 {
  strings:
    $o0 = "off_41D13C" wide ascii nocase
    $o1 = "DP3xK" wide ascii nocase
    $o2 = "off_41D154" wide ascii nocase
    $o3 = "off_41D148" wide ascii nocase
    $o4 = "xB351F353" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726140321_5131 {
  strings:
    $o0 = "EnableScrollBar" wide ascii nocase
    $o1 = "CpDyuOUXrcwOH4" wide ascii nocase
    $o2 = "vflve6OkSQFJduaCB" wide ascii nocase
    $o3 = "vqNtDxhIkHL" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726140325_8835 {
  condition:
    auto_rule_20250726140318_2194 or auto_rule_20250726140321_5131
}