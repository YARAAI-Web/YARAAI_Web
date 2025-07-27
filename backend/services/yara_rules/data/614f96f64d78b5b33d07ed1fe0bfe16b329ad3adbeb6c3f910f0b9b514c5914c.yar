rule auto_rule_20250726171911_1809 {
  strings:
    $o0 = "hwinsta" wide ascii nocase
    $o1 = "GetCaretBlinkTime" wide ascii nocase
    $o2 = "GetKBCodePage" wide ascii nocase
    $o3 = "lpszSrc" wide ascii nocase
    $o4 = "dwFlagsAndAttributes" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726171914_9406 {
  strings:
    $o0 = "MapVirtualKeyExA" wide ascii nocase
    $o1 = "cAccelEntries" wide ascii nocase
    $o2 = "FileTimeToDosDateTime" wide ascii nocase
    $o3 = "wHow" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726171918_2724 {
  condition:
    auto_rule_20250726171911_1809 or auto_rule_20250726171914_9406
}