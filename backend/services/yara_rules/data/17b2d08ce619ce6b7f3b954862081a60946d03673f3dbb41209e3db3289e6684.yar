rule auto_rule_20250727014317_3248 {
  strings:
    $o0 = "idHook" wide ascii nocase
    $o1 = "dword_41DB40" wide ascii nocase
    $o2 = "NotificationFilter" wide ascii nocase
  condition:
    3 of ($o*)
}