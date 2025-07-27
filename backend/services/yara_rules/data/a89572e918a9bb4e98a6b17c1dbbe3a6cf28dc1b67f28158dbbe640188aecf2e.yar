rule auto_rule_20250726144926_7511 {
  strings:
    $o0 = "off_461078" wide ascii nocase
    $o1 = "xFF000000" wide ascii nocase
    $o2 = "_tmpfname" wide ascii nocase
    $o3 = "nProgram" wide ascii nocase
    $o4 = "dword_461518" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726144929_1391 {
  strings:
    $o0 = "dword_461560" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726144932_3750 {
  condition:
    auto_rule_20250726144926_7511 or auto_rule_20250726144929_1391
}