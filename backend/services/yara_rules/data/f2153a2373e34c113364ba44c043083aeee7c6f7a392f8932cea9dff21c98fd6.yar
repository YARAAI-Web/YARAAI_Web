rule auto_rule_20250726061946_4315 {
  strings:
    $o0 = "pstr" wide ascii nocase
    $o1 = "achPath" wide ascii nocase
    $o2 = "StrRetToBufW" wide ascii nocase
    $o3 = "fIgnoreHKCU" wide ascii nocase
    $o4 = "bScan" wide ascii nocase
  condition:
    4 of ($o*)
}