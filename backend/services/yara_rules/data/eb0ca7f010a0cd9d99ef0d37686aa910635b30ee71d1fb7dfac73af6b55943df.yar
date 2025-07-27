rule auto_rule_20250726174140_5876 {
  strings:
    $o0 = "cchBuff" wide ascii nocase
    $o1 = "pszBuf" wide ascii nocase
    $o2 = "MapVirtualKeyA" wide ascii nocase
    $o3 = "StrToIntW" wide ascii nocase
  condition:
    4 of ($o*)
}