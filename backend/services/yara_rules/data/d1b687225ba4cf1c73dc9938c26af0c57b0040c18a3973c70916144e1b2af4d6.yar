rule auto_rule_20250726191058_2859 {
  strings:
    $o0 = "SHRegEnumUSKeyW" wide ascii nocase
    $o1 = "iModeNum" wide ascii nocase
    $o2 = "pszRoot" wide ascii nocase
    $o3 = "hdcDst" wide ascii nocase
    $o4 = "LoadBitmapW" wide ascii nocase
  condition:
    4 of ($o*)
}