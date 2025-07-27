rule auto_rule_20250726074405_9453 {
  strings:
    $o0 = "gu_return" wide ascii nocase
    $o1 = "_seh_longjmp_unwind" wide ascii nocase
    $o2 = "dword_450004" wide ascii nocase
    $o3 = "dword_45D504" wide ascii nocase
    $o4 = "dword_45D538" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726074407_0878 {
  strings:
    $o0 = "dword_45D53C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726074411_1584 {
  condition:
    auto_rule_20250726074405_9453 or auto_rule_20250726074407_0878
}