rule auto_rule_20250726154343_0731 {
  strings:
    $o0 = "xB23B8F09EDAED898uLL" wide ascii nocase
    $o1 = "qword_4295AC" wide ascii nocase
    $o2 = "xB23B8F09" wide ascii nocase
    $o3 = "dword_429991" wide ascii nocase
    $o4 = "xEDAAD89B" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726154346_4313 {
  strings:
    $o0 = "dword_4294C8" wide ascii nocase
    $o1 = "xFEAB" wide ascii nocase
    $o2 = "dword_42965C" wide ascii nocase
    $o3 = "x5627" wide ascii nocase
    $o4 = "dword_429504" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726154351_7744 {
  condition:
    auto_rule_20250726154343_0731 or auto_rule_20250726154346_4313
}