rule auto_rule_20250726101446_1298 {
  strings:
    $o0 = "tail_loop_start" wide ascii nocase
    $o1 = "strpbrk" wide ascii nocase
    $o2 = "algn_4760B2" wide ascii nocase
    $o3 = "mapping" wide ascii nocase
    $o4 = "dword_475E50" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726101449_0311 {
  strings:
    $o0 = "dword_475F9C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726101453_3483 {
  condition:
    auto_rule_20250726101446_1298 or auto_rule_20250726101449_0311
}