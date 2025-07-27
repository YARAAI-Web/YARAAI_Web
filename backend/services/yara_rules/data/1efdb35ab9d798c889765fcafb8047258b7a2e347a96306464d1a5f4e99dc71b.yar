rule auto_rule_20250727012755_4225 {
  strings:
    $o0 = "dword_100BA400" wide ascii nocase
    $o1 = "dword_100BA428" wide ascii nocase
    $o2 = "dword_100B9DDC" wide ascii nocase
  condition:
    3 of ($o*)
}