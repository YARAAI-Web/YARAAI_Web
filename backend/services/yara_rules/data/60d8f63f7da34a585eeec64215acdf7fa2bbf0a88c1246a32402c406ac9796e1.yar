rule auto_rule_20250726224953_7287 {
  strings:
    $o0 = "dword_411980" wide ascii nocase
    $o1 = "TrailDown0" wide ascii nocase
    $o2 = "_global_unwind2" wide ascii nocase
    $o3 = "UnwindUp6_0" wide ascii nocase
    $o4 = "dword_411958" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726224956_9710 {
  strings:
    $o0 = "dword_4119AC" wide ascii nocase
    $o1 = "dword_411E44" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726225000_6049 {
  condition:
    auto_rule_20250726224953_7287 or auto_rule_20250726224956_9710
}