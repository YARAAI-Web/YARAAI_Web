rule auto_rule_20250727005313_4145 {
  strings:
    $o0 = "CallMsgFilterW" wide ascii nocase
    $o1 = "x19000u" wide ascii nocase
  condition:
    all of them
}