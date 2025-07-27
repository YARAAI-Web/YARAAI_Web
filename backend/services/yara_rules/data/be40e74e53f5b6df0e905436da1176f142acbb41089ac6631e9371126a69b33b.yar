rule auto_rule_20250726080503_7827 {
  strings:
    $o0 = "GetModule" wide ascii nocase
    $o1 = "level" wide ascii nocase
    $o2 = "CORDebuggerAttached" wide ascii nocase
    $o3 = "MatchAnyKeyword" wide ascii nocase
    $o4 = "dynamic_atexit_destructor_for__ProfilingAPIDetach" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726080505_1869 {
  strings:
    $o0 = "BinderClassID" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726080508_4333 {
  condition:
    auto_rule_20250726080503_7827 or auto_rule_20250726080505_1869
}