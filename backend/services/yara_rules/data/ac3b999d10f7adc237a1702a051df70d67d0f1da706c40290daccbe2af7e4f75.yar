rule auto_rule_20250726200659_8830 {
  strings:
    $o0 = "PropertySheetPageW" wide ascii nocase
    $o1 = "xF89C853D" wide ascii nocase
    $o2 = "x2BE2" wide ascii nocase
    $o3 = "x1B76" wide ascii nocase
    $o4 = "x64FCu" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726200702_6348 {
  strings:
    $o0 = "x6F04" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726200706_3346 {
  condition:
    auto_rule_20250726200659_8830 or auto_rule_20250726200702_6348
}