rule auto_rule_20250726201736_2955 {
  strings:
    $o0 = "UnwindUp1_0" wide ascii nocase
    $o1 = "dword_460774" wide ascii nocase
    $o2 = "__crtGetEnvironmentStringsA" wide ascii nocase
    $o3 = "byte_4617C0" wide ascii nocase
    $o4 = "dword_460734" wide ascii nocase
  condition:
    4 of ($o*)
}