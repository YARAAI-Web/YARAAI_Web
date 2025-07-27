rule auto_rule_20250726203331_5113 {
  strings:
    $o0 = "TrailUp0_0" wide ascii nocase
    $o1 = "dword_476C38" wide ascii nocase
    $o2 = "dword_42F008" wide ascii nocase
    $o3 = "finish_loop" wide ascii nocase
    $o4 = "memcpy_0" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726203334_5293 {
  strings:
    $o0 = "__sbh_alloc_new_region" wide ascii nocase
    $o1 = "dword_477050" wide ascii nocase
    $o2 = "dword_476EE4" wide ascii nocase
    $o3 = "gu_return" wide ascii nocase
    $o4 = "dword_476F14" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726203339_3492 {
  condition:
    auto_rule_20250726203331_5113 or auto_rule_20250726203334_5293
}