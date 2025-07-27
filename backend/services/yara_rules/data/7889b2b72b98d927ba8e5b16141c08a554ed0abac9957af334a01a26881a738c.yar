rule auto_rule_20250726231236_8704 {
  strings:
    $o0 = "dword_449964" wide ascii nocase
    $o1 = "main_loop_1" wide ascii nocase
    $o2 = "memcpy_0" wide ascii nocase
    $o3 = "UnwindUp1_0" wide ascii nocase
    $o4 = "GetStringTypeA" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726231239_4775 {
  strings:
    $o0 = "dword_449A80" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726231250_7041 {
  condition:
    auto_rule_20250726231236_8704 or auto_rule_20250726231239_4775
}