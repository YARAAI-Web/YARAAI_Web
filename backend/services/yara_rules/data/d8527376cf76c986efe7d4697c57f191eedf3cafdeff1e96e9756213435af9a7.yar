rule auto_rule_20250726102438_1858 {
  strings:
    $o0 = "_NLG_Notify" wide ascii nocase
    $o1 = "dword_4563B8" wide ascii nocase
  condition:
    all of them
}