rule auto_rule_20250726140247_9468 {
  strings:
    $o0 = "xF89C8532" wide ascii nocase
    $o1 = "dword_430435" wide ascii nocase
    $o2 = "CreatePalette" wide ascii nocase
    $o3 = "off_4121A8" wide ascii nocase
    $o4 = "dword_430451" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726140250_2139 {
  strings:
    $o0 = "x780B" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726140254_3470 {
  condition:
    auto_rule_20250726140247_9468 or auto_rule_20250726140250_2139
}