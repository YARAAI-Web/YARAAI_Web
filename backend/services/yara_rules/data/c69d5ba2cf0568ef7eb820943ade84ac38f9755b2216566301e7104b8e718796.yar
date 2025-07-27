rule auto_rule_20250727002129_4720 {
  strings:
    $o0 = "GetOpenFileNameW" wide ascii nocase
    $o1 = "dword_4C1138" wide ascii nocase
    $o2 = "ImageList_Create" wide ascii nocase
    $o3 = "off_4B1858" wide ascii nocase
  condition:
    4 of ($o*)
}