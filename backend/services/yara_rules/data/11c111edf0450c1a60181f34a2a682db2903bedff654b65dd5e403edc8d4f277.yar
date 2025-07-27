rule auto_rule_20250727024225_3144 {
  strings:
    $o0 = "IntersectClipRect" wide ascii nocase
    $o1 = "InSendMessageEx" wide ascii nocase
    $o2 = "x5787u" wide ascii nocase
    $o3 = "x6DF5u" wide ascii nocase
    $o4 = "IsWindowEnabled" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250727024228_0453 {
  strings:
    $o0 = "dword_433623" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250727024233_5967 {
  condition:
    auto_rule_20250727024225_3144 or auto_rule_20250727024228_0453
}