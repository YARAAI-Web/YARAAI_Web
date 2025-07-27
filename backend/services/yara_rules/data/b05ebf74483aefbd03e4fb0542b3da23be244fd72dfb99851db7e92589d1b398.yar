rule auto_rule_20250726091324_3109 {
  strings:
    $o0 = "_filbuf" wide ascii nocase
    $o1 = "flAllocationType" wide ascii nocase
    $o2 = "__crtGetEnvironmentStringsA" wide ascii nocase
    $o3 = "_ioinit" wide ascii nocase
    $o4 = "UnwindUp2_0" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250726091327_2001 {
  strings:
    $o0 = "x41C4u" wide ascii nocase
    $o1 = "dword_410504" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726091337_2803 {
  condition:
    auto_rule_20250726091324_3109 or auto_rule_20250726091327_2001
}