rule auto_rule_20250726232313_6301 {
  strings:
    $o0 = "__crtMessageBoxA" wide ascii nocase
    $o1 = "main_loop_entrance_0" wide ascii nocase
    $o2 = "_cinit" wide ascii nocase
    $o3 = "UnwindUp4_0" wide ascii nocase
    $o4 = "byte_45D580" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726232316_5902 {
  strings:
    $o0 = "dword_45CFCC" wide ascii nocase
    $o1 = "byte_45D080" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726232327_5050 {
  condition:
    auto_rule_20250726232313_6301 or auto_rule_20250726232316_5902
}