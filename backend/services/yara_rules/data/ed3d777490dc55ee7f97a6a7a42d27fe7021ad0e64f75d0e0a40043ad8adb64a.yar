rule auto_rule_20250727041146_3428 {
  strings:
    $o0 = "TrailDown2" wide ascii nocase
    $o1 = "UnwindUp5_0" wide ascii nocase
    $o2 = "RtlUnwind" wide ascii nocase
    $o3 = "_ioinit" wide ascii nocase
    $o4 = "byte_45D681" wide ascii nocase
  condition:
    5 of ($o*)
}