rule auto_rule_20250726064502_4325 {
  strings:
    $o0 = "WindowFromPoint" wide ascii nocase
    $o1 = "hData" wide ascii nocase
    $o2 = "WINNLSGetEnableStatus" wide ascii nocase
  condition:
    3 of ($o*)
}