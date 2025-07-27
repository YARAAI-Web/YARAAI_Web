rule auto_rule_20250727040235_6438 {
  strings:
    $o0 = "xC0000092" wide ascii nocase
    $o1 = "off_463CD4" wide ascii nocase
    $o2 = "UnwindUp5_0" wide ascii nocase
    $o3 = "dword_464308" wide ascii nocase
    $o4 = "fields" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727040238_0741 {
  strings:
    $o0 = "dword_463AAC" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727040241_6211 {
  condition:
    auto_rule_20250727040235_6438 or auto_rule_20250727040238_0741
}