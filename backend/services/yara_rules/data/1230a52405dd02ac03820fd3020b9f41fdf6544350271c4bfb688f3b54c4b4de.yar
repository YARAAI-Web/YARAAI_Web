rule auto_rule_20250726213325_0587 {
  strings:
    $o0 = "UrlCreateFromPathW" wide ascii nocase
    $o1 = "uFiletype" wide ascii nocase
    $o2 = "dwDesiredAccess" wide ascii nocase
  condition:
    3 of ($o*)
}