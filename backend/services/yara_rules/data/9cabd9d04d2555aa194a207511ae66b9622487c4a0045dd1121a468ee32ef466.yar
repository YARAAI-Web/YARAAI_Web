rule auto_rule_20250726154802_1462 {
  strings:
    $o0 = "dword_43468F" wide ascii nocase
    $o1 = "dword_4346C7" wide ascii nocase
    $o2 = "dword_4346BB" wide ascii nocase
    $o3 = "CreateDIBitmap" wide ascii nocase
    $o4 = "FindWindowExA" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726154805_3079 {
  strings:
    $o0 = "off_434733" wide ascii nocase
    $o1 = "iUsage" wide ascii nocase
    $o2 = "lpmiia" wide ascii nocase
  condition:
    3 of ($o*)
}

rule combined_rule_20250726154808_6669 {
  condition:
    auto_rule_20250726154802_1462 or auto_rule_20250726154805_3079
}