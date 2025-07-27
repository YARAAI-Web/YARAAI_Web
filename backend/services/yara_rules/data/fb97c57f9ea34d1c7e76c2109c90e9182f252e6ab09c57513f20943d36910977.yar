rule auto_rule_20250727033354_5727 {
  strings:
    $o0 = "x7FFF" wide ascii nocase
    $o1 = "dword_4C1278" wide ascii nocase
    $o2 = "WinTitleMatchMode" wide ascii nocase
  condition:
    3 of ($o*)
}