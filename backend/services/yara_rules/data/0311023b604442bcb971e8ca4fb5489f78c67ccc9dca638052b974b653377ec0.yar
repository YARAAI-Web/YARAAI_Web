rule auto_rule_20250727042843_5908 {
  strings:
    $o0 = "_Copy_s" wide ascii nocase
    $o1 = "dword_10086D94" wide ascii nocase
    $o2 = "Destinationa" wide ascii nocase
  condition:
    3 of ($o*)
}