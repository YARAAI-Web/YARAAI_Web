rule auto_rule_20250726130831_1260 {
  strings:
    $o0 = "xC000008E" wide ascii nocase
    $o1 = "UnwindUp3_0" wide ascii nocase
    $o2 = "main_loop_entrance_0" wide ascii nocase
    $o3 = "_flushall" wide ascii nocase
    $o4 = "nFile" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726130834_4903 {
  strings:
    $o0 = "Dumping" wide ascii nocase
    $o1 = "write_string" wide ascii nocase
    $o2 = "_heap_alloc_dbg" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726130843_8005 {
  condition:
    auto_rule_20250726130831_1260 or auto_rule_20250726130834_4903
}