rule auto_rule_20250726184455_6196 {
  strings:
    $o0 = "FontFamilyFromName" wide ascii nocase
    $o1 = "dword_4596B8" wide ascii nocase
  condition:
    all of them
}