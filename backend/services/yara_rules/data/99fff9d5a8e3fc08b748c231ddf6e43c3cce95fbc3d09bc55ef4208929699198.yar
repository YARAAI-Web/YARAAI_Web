rule auto_rule_20250726223141_0604 {
  strings:
    $o0 = "dword_412228" wide ascii nocase
    $o1 = "dword_40E000" wide ascii nocase
    $o2 = "TrailDown0" wide ascii nocase
    $o3 = "ReturnValue" wide ascii nocase
    $o4 = "UnwindUp5_0" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726223144_2319 {
  strings:
    $o0 = "byte_411D94" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726223157_9189 {
  condition:
    auto_rule_20250726223141_0604 or auto_rule_20250726223144_2319
}