rule auto_rule_20250727025637_8551 {
  strings:
    $o0 = "TrailDown0" wide ascii nocase
    $o1 = "UnwindUp4_0" wide ascii nocase
    $o2 = "dword_42089C" wide ascii nocase
    $o3 = "ActiveWindow" wide ascii nocase
    $o4 = "terminated" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250727025641_9509 {
  strings:
    $o0 = "_msize" wide ascii nocase
    $o1 = "RtlUnwind" wide ascii nocase
    $o2 = "dword_42064C" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250727025653_1146 {
  condition:
    auto_rule_20250727025637_8551 or auto_rule_20250727025641_9509
}