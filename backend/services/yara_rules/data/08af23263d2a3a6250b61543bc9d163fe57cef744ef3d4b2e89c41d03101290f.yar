rule auto_rule_20250727044033_0473 {
  strings:
    $o0 = "_cpinfo" wide ascii nocase
    $o1 = "dbgrpt" wide ascii nocase
    $o2 = "SetConsoleMode" wide ascii nocase
  condition:
    3 of ($o*)
}