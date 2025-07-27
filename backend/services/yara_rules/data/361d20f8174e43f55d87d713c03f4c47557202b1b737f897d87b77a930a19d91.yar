rule auto_rule_20250726135359_4740 {
  strings:
    $o0 = "FontFamilyFromName" wide ascii nocase
    $o1 = "off_44DD0C" wide ascii nocase
    $o2 = "dword_44E178" wide ascii nocase
    $o3 = "off_44D578" wide ascii nocase
  condition:
    4 of ($o*)
}