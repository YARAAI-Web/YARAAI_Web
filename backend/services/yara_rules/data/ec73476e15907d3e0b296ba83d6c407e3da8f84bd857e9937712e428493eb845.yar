rule auto_rule_20250726114701_9380 {
  strings:
    $o0 = "GetMenuItemInfoW" wide ascii nocase
    $o1 = "DdeQueryStringA" wide ascii nocase
    $o2 = "uFiletype" wide ascii nocase
    $o3 = "ulOptions" wide ascii nocase
    $o4 = "puiLo" wide ascii nocase
  condition:
    4 of ($o*)
}