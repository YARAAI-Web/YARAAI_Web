rule auto_rule_20250727035915_5656 {
  strings:
    $o0 = "strcat" wide ascii nocase
    $o1 = "UnwindUp6_0" wide ascii nocase
    $o2 = "dword_4602AC" wide ascii nocase
    $o3 = "RtlUnwind" wide ascii nocase
  condition:
    4 of ($o*)
}