rule auto_rule_20250726071356_4892 {
  strings:
    $o0 = "FontFamilyFromName" wide ascii nocase
    $o1 = "dword_455CD8" wide ascii nocase
  condition:
    all of them
}