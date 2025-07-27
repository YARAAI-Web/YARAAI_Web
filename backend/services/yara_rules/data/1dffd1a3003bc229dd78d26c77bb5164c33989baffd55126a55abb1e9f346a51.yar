rule auto_rule_20250726205348_6002 {
  strings:
    $o0 = "pthreadmbcinfo" wide ascii nocase
    $o1 = "dword_40A1A4" wide ascii nocase
  condition:
    all of them
}