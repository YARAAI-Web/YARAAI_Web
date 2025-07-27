rule auto_rule_20250726190709_5914 {
  strings:
    $o0 = "lpszShortPath" wide ascii nocase
    $o1 = "hrgnUpdate" wide ascii nocase
    $o2 = "GetConsoleAliasExesW" wide ascii nocase
    $o3 = "nStdHandle" wide ascii nocase
    $o4 = "pszItemText" wide ascii nocase
  condition:
    4 of ($o*)
}