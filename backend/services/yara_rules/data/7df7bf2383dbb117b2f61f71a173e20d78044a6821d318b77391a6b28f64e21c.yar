rule auto_rule_20250727032902_0169 {
  strings:
    $o0 = "dword_45D8A8" wide ascii nocase
    $o1 = "UnwindUp4_0" wide ascii nocase
    $o2 = "main_loop_entrance" wide ascii nocase
    $o3 = "doexit" wide ascii nocase
    $o4 = "byte_45D3EC" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727032905_7682 {
  strings:
    $o0 = "dword_45D554" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727032909_5344 {
  condition:
    auto_rule_20250727032902_0169 or auto_rule_20250727032905_7682
}