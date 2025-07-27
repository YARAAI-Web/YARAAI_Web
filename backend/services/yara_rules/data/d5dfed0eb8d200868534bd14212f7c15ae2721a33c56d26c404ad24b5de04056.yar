rule auto_rule_20250727004600_8955 {
  strings:
    $o0 = "xcptlookup" wide ascii nocase
    $o1 = "dword_411EA8" wide ascii nocase
    $o2 = "TrailUp0_0" wide ascii nocase
    $o3 = "finish_loop" wide ascii nocase
    $o4 = "__crtGetEnvironmentStringsA" wide ascii nocase
  condition:
    5 of ($o*)
}

rule auto_rule_20250727004604_0289 {
  strings:
    $o0 = "dword_411984" wide ascii nocase
    $o1 = "_abnormal_termination" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727004616_4564 {
  condition:
    auto_rule_20250727004600_8955 or auto_rule_20250727004604_0289
}