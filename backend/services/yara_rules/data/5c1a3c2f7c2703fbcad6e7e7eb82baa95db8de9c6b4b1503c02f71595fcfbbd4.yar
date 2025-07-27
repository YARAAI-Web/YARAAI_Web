rule auto_rule_20250726135937_7449 {
  strings:
    $o0 = "EnableMenuItem" wide ascii nocase
    $o1 = "DrawEdge" wide ascii nocase
    $o2 = "GetShellWindow" wide ascii nocase
    $o3 = "uFiletype" wide ascii nocase
    $o4 = "lpmii" wide ascii nocase
  condition:
    5 of ($o*)
}