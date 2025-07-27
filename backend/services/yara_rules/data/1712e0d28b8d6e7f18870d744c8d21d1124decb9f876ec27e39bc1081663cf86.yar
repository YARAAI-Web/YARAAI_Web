rule auto_rule_20250726185640_3415 {
  strings:
    $o0 = "pDst" wide ascii nocase
    $o1 = "StrStrA" wide ascii nocase
    $o2 = "SHRegCloseUSKey" wide ascii nocase
    $o3 = "pszContentType" wide ascii nocase
    $o4 = "hWndServer" wide ascii nocase
  condition:
    4 of ($o*)
}