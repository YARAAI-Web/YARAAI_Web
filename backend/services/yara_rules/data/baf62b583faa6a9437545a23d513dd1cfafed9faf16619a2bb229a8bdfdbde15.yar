rule auto_rule_20250726140049_5362 {
  strings:
    $o0 = "off_460D74" wide ascii nocase
    $o1 = "memcpy_0" wide ascii nocase
    $o2 = "dword_461544" wide ascii nocase
    $o3 = "xFF000000" wide ascii nocase
  condition:
    4 of ($o*)
}