rule auto_rule_20250726210118_3387 {
  strings:
    $o0 = "dword_466778" wide ascii nocase
    $o1 = "pSid2" wide ascii nocase
    $o2 = "Runtime" wide ascii nocase
    $o3 = "_ioinit" wide ascii nocase
    $o4 = "UnwindUp6_0" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726210122_2270 {
  strings:
    $o0 = "algn_4675F2" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726210132_8666 {
  condition:
    auto_rule_20250726210118_3387 or auto_rule_20250726210122_2270
}