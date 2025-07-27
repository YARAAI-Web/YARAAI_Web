rule auto_rule_20250726233915_1460 {
  strings:
    $o0 = "dword_46062C" wide ascii nocase
    $o1 = "dword_460138" wide ascii nocase
    $o2 = "UnwindUp4_0" wide ascii nocase
    $o3 = "dword_4602AC" wide ascii nocase
  condition:
    4 of ($o*)
}