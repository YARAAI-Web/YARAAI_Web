rule auto_rule_20250726084946_0349 {
  strings:
    $o0 = "dword_449C68" wide ascii nocase
    $o1 = "UnwindUp1_0" wide ascii nocase
    $o2 = "CPtoLCID" wide ascii nocase
  condition:
    3 of ($o*)
}