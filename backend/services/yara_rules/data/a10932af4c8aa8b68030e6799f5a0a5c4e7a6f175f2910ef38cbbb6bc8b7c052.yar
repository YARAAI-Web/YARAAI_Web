rule auto_rule_20250726105823_6553 {
  strings:
    $o0 = "LibraryA" wide ascii nocase
    $o1 = "ProcessWindowStation" wide ascii nocase
    $o2 = "off_476D04" wide ascii nocase
    $o3 = "_mtdeletelocks" wide ascii nocase
    $o4 = "off_4765BC" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726105826_7204 {
  strings:
    $o0 = "x415620" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726105830_1489 {
  condition:
    auto_rule_20250726105823_6553 or auto_rule_20250726105826_7204
}