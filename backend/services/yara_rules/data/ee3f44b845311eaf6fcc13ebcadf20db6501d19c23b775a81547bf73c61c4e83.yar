rule auto_rule_20250727012511_7776 {
  strings:
    $o0 = "__acrt_FlsGetValue" wide ascii nocase
    $o1 = "dword_414B34" wide ascii nocase
  condition:
    all of them
}