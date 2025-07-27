rule auto_rule_20250726221408_5739 {
  strings:
    $o0 = "x396Bu" wide ascii nocase
    $o1 = "ResizePalette" wide ascii nocase
    $o2 = "tagBITMAPINFO" wide ascii nocase
    $o3 = "dword_435E0A" wide ascii nocase
    $o4 = "lpbmi" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726221412_9000 {
  strings:
    $o0 = "UserTime" wide ascii nocase
    $o1 = "CommConfig" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726221415_5464 {
  condition:
    auto_rule_20250726221408_5739 or auto_rule_20250726221412_9000
}