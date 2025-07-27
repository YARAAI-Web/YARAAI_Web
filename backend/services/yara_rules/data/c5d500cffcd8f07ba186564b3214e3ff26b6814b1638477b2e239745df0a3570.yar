rule auto_rule_20250726222424_8301 {
  strings:
    $o0 = "x402821" wide ascii nocase
    $o1 = "dword_449AC0" wide ascii nocase
    $o2 = "dword_44A3B0" wide ascii nocase
    $o3 = "off_449A40" wide ascii nocase
    $o4 = "dword_44A044" wide ascii nocase
  condition:
    4 of ($o*)
}