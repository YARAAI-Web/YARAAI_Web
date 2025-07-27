rule auto_rule_20250727034702_1463 {
  strings:
    $o0 = "lpModemStat" wide ascii nocase
    $o1 = "lpszCurrent" wide ascii nocase
    $o2 = "dwBufferCoord" wide ascii nocase
  condition:
    3 of ($o*)
}