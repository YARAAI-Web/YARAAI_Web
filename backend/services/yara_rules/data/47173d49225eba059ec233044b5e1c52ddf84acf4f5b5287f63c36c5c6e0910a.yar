rule auto_rule_20250726171630_9396 {
  strings:
    $o0 = "SwitchDesktop" wide ascii nocase
    $o1 = "DestroyCaret" wide ascii nocase
    $o2 = "GetAltTabInfoW" wide ascii nocase
    $o3 = "nIDLastButton" wide ascii nocase
  condition:
    4 of ($o*)
}