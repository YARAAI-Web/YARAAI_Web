rule auto_rule_20250727043149_9342 {
  strings:
    $o0 = "LookupIconIdFromDirectoryEx" wide ascii nocase
    $o1 = "pvInfo" wide ascii nocase
    $o2 = "GetScrollPos" wide ascii nocase
    $o3 = "GetOpenClipboardWindow" wide ascii nocase
    $o4 = "pszOut" wide ascii nocase
  condition:
    4 of ($o*)
}